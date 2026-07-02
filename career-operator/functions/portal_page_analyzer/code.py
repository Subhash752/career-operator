#input_type_name: PortalPageAnalyzerInput
#output_type_name: PortalPageAnalyzerResult
#function_name: portal_page_analyzer

import json, urllib.request
from html.parser import HTMLParser
from pydantic import BaseModel
from lemma_sdk import FunctionContext


class PortalPageAnalyzerInput(BaseModel):
    url: str


class PortalField(BaseModel):
    name: str = ""
    type: str = "text"
    id: str = ""
    label: str = ""
    placeholder: str = ""
    required: bool = False
    autocomplete: str = ""


class PortalPageAnalyzerResult(BaseModel):
    success: bool = False
    fields: list[PortalField] = []
    field_count: int = 0
    forms_found: int = 0
    error: str = ""
    note: str = ""


class FormFieldParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.fields = []
        self.in_form = False
        self.form_count = 0
        self.label_text = ""
        self.current_tag = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.current_tag = tag
        if tag == "form":
            self.in_form = True
            self.form_count += 1
        if self.in_form and tag == "input":
            self._add_field(a, a.get("type", "text"))
        if self.in_form and tag == "select":
            self._add_field(a, "select")
        if self.in_form and tag == "textarea":
            self._add_field(a, "textarea")
        self.label_text = ""

    def _add_field(self, a, ftype):
        fname = a.get("name", "")
        fid = a.get("id", "")
        field = PortalField(
            name=fname,
            type=ftype,
            id=fid,
            label=self.label_text.strip(),
            placeholder=a.get("placeholder", ""),
            required="required" in a or a.get("aria-required") == "true",
            autocomplete=a.get("autocomplete", ""),
        )
        if fname or fid:
            self.fields.append(field)

    def handle_data(self, data):
        if self.current_tag == "label":
            self.label_text = (self.label_text + " " + data.strip()).strip()

    def handle_endtag(self, tag):
        if tag == "form":
            self.in_form = False
        self.current_tag = None


async def portal_page_analyzer(ctx: FunctionContext, data: PortalPageAnalyzerInput) -> PortalPageAnalyzerResult:
    url = data.url
    if not url:
        return PortalPageAnalyzerResult(success=False, error="No URL provided")
    try:
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            },
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode("utf-8", errors="replace")
        parser = FormFieldParser()
        parser.feed(html)
        return PortalPageAnalyzerResult(
            success=True,
            fields=parser.fields,
            field_count=len(parser.fields),
            forms_found=parser.form_count,
            note="Fields extracted from server-rendered HTML. JS-rendered forms (React, Angular, Vue) may not be detected.",
        )
    except Exception as e:
        return PortalPageAnalyzerResult(
            success=False,
            error=str(e),
            note="Could not fetch or parse the portal page. It may require authentication or use JavaScript rendering.",
        )
