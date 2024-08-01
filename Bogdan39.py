user_profile = {
    'name': 'Ivan',
    'comments_qty': 23,
}

def user_info(name, comments_qty=0):
    if not comments_qty:
        return f'{name} has no comments'
    
    return f'{name} has {comments_qty} comments'

print(user_info(**user_profile))