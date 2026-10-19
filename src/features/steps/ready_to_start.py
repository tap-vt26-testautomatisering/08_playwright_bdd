from behave.api.pending_step import StepNotImplementedError
from behave import when, then
from playwright.sync_api import expect


@when(u'vi har spelaren "{name}"')
def step_impl(context, name):
    context.base_page.add_player(name)


@then(u'knappen Börja ditt drag syns')
def step_impl(context):
    expect(context.base_page.start_turn_button).to_be_visible()
