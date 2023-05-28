import cv2

def load_images():
    images = [
        "data/templates/spore.png",
        "data/templates/battle/fight.png",
        'data/templates/text_period.png',
        "data/templates/oh_a_bite.png",
        "data/templates/on_the_hook.png",
        "data/templates/not_even_a_nibble.png",
        "data/templates/it_got_away.png",
        'data/templates/battle/run.png'  ]
    image_dict = {}
    for image in images:
        image_dict[image] = cv2.imread(image, cv2.IMREAD_UNCHANGED)
    return image_dict
    
image_dict = load_images()