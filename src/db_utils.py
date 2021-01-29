from confdb import Pad, session
def add_pad(title, content, tags=[]):
    try:
        if type(title) != type(str) and type(content) != type(str) and title != '' and content != '':
            new_pad = Pad(title=title, content=content)
            session.add(new_pad)
            session.commit()
            return new_pad

    except Exception:
        print(">>>>>>>>>>Error add to DB<<<<<<<<<<<<")
