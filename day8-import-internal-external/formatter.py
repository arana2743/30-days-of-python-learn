template_msg = """
Hello {name},
We are excited to have you onboard!
"""

def format_msg(name="John", website="gitlab.co"):
    my_msg = template_msg.format(name=name, website=website)
    return my_msg
