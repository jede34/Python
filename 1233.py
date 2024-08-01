from collections import deque

backward_history = deque(['New Tab'])
forward_history = deque()



def browse_to(website_name):
    backward_history.append(website_name)
    forward_history.clear()


def go_backward():
    if len(backward_history) > 1:
        last_visited_site = backward_history.pop()
        forward_history.append(last_visited_site)


def go_forward():
    last_visited_site = forward_history.pop()
    backward_history.append(last_visited_site)


def get_current_site():
    current_website = backward_history.pop()
    backward_history.append(current_website)
    return current_website

print(get_current_site())
browse_to('Google')
print(get_current_site())
browse_to('Wiki')
print(get_current_site())
go_backward()
print(get_current_site())
go_forward()
print(get_current_site())
