def get_posts_info(**person):
    print(person)

    print(type(person))
    info = {
        f'{person['name']} wrote'
        f'{person['posts_qty']} posts'
        f'{person['lala']} lala'
    }
    return info

info = get_posts_info(name='Ivan', posts_qty=25, lala= True)
print(info)