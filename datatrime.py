from datetime import date


def get_weekday():
    return date.today().strftime('%A')


def create_new_post(post, weekday=get_weekday()):
    post_copy = post
    post_copy['created_on_weekday'] = weekday
    return post_copy

initial_post = {
    'id': 243,
    'author': 'Ivan',
}

post_with_weekday = create_new_post(initial_post, 'Monday')

print(post_with_weekday)

print(initial_post)