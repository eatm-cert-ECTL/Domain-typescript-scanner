from typing import Any
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage
import datetime
import os
from pathlib import Path

REPORTS_FOLDER = "reports"

def load_template(tpl:Path=Path('templates','template.docx')) -> DocxTemplate:
	return DocxTemplate(tpl)

def generate_report(context:dict[str, Any],template:DocxTemplate) -> Path:
	template.render(context)
	path = Path(REPORTS_FOLDER , 'ECAW-001-{}-Warning against potentially fraudulent website impersonating {}.docx'.format(context['Year'],context['Stakeholder']))
	if not os.path.isdir(REPORTS_FOLDER):
		os.mkdir(REPORTS_FOLDER)
	template.save(path)
	return path
	
def gen_context(screenshot_path,
		template,
		Stakeholder="",
		Ref="",
		Version="1.0",
		Fraudulent_website="",
		Threat_motive="Cyber Crime",
		Threat_level="Low",
		Threat_actor="N/A",
		Threat_attribution="N/A",
		Threat_taxonomy="Nefarious Activity / Abuse",
		Threat_sub_taxonomy="Phishing attacks / Spear phishing attacks",
		Target_domain="Global",
		Target_sectors="Aviation Sector",
		Target_specific="N/A",
		UUID="",
		whoisJson="") -> dict[str, Any]:

	image = InlineImage(template,image_descriptor=screenshot_path, width=Cm(17), height=Cm(10))
	context = {
		'Stakeholder': Stakeholder,
		'Ref': f"ECAW-00-{datetime.datetime.now().strftime('%Y')}",
		'Day': datetime.datetime.now().strftime('%d'),
		'Month': datetime.datetime.now().strftime('%m'),
		'Year': datetime.datetime.now().strftime('%Y'),
		'Version': Version,
		'Fraudulent_website': Fraudulent_website,
		'Threat_motive': Threat_motive,
		'Threat_level': Threat_level,
		'Threat_actor': Threat_actor,
		'Threat_attribution': Threat_attribution,
		'Threat_taxonomy': Threat_taxonomy,
		'Threat_sub_taxonomy': Threat_sub_taxonomy,
		"Target_domain": Target_domain,
		"Target_sectors": Target_sectors,
		"Target_specific": Target_specific,
		"UUID": UUID,
		"Capture": image,
		"Whois": whoisJson
	}
	return context

if __name__ == "__main__":
	template = load_template()
	generate_report(gen_context("screenshots/abcde.com.png",template),template)