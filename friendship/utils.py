from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import render_to_string, get_template
# email import :
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.conf import settings


def send_email(subject, to_email, friend_request, context=None, html_template_path=None):
    """
    Send email with html content, context and attachement/embedded images.
    """
    # embedding image:
    # Load the image you want to send as bytes
    img_data = None
    # use profile photo if available
    try:
        img_data = open(friend_request.friendship.user.profile.photo.url, 'rb').read()
    except:
        img_data = open('static/images/avatar.jpg', 'rb').read()

    # Create a "related" message container that will hold the HTML 
    # message and the image. These are "related" (not "alternative")
    # because they are different, unique parts of the HTML message,
    # not alternative (html vs. plain text) views of the same content.
    html_part = MIMEMultipart(_subtype='related')

    # Create the body with HTML. Note that the image, since it is inline, is 
    # referenced with the URL cid:friend_image... you should take care to make
    # "friend_image" unique
 
    html_content = get_template(
        html_template_path
        ).render(context)
    body = MIMEText(html_content, _subtype='html')
    html_part.attach(body)


    # Now create the MIME container for the image
    img = MIMEImage(img_data, 'jpeg')
    img.add_header('Content-Id', '<friend_image>')  # angle brackets are important
    img.add_header("Content-Disposition", "inline", filename="friend_image")
    html_part.attach(img)
    # to create an alternative part for this message
    msg = EmailMessage(
        subject,
        None,
        f"{settings.SITE_NAME}<{settings.EMAIL_HOST_USER}>",
        to_email,
    )
    msg.attach(html_part) # Attach the raw MIMEBase descendant. This is a public method on EmailMessage
    msg.send()