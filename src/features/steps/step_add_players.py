import re
from behave import given, when, then
from behave.api.pending_step import StepNotImplementedError


@given(u'vi är på startsidan')
def step_impl(context):
    context.page.goto(context.base_url, timeout=10_000)


@when(u'jag klickar på "Lägg till spelare"')
def step_impl(context):
    # Tyvärr finns inget test_id så vi får använda role+text
    context.page.get_by_role("button", name="Lägg till spelare").click()


@when(u'jag skriver in spelarnamn "{name}"')
def step_impl(context, name):
    # Eftersom det bara finns ett <input> kan vi välja ut den så här. Alternativt kan vi använda: locator("#player-name") för att välja ut baserat på HTML-id.
    context.page.get_by_role("textbox").fill(name)


@then(u'spelarens namn "{name}" ska visas på sidan')
def step_impl(context, name):
    pattern = re.compile(rf"{re.escape(name)}\s+0:00\.0")
    context.page.get_by_text(pattern)

