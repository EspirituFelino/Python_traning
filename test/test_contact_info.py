from random import randrange
from model.contact import Contact


def test_contact_info_from_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name='Test', last_name='Test'))
    contact_list = app.contact.get_contact_list()
    index = randrange(len(contact_list))
    contact_from_home_page = contact_list[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.first_name == contact_from_edit_page.first_name
    assert contact_from_home_page.last_name == contact_from_edit_page.last_name
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_homepage == contact_from_edit_page.merge_phones_like_homepage()
    assert contact_from_home_page.all_emails_from_homepage == contact_from_edit_page.merge_emails_like_homepage()
