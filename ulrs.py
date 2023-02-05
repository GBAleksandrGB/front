from views import Index, Contacts


routes = {
    '/': Index(),
    '/contacts/': Contacts(),
}
