from django.db import models
from django.utils.translation import ugettext_lazy as _


class SocialLinkMixin(models.Model):

    LINK_TYPE_CHOICES = (
        ('fac', 'facebook'),
        ('twi', 'twitter'),
        ('quo', 'quora'),
        ('wik', 'wikipedia'),
        ('lin', 'linkedin'),
        ('blo', 'blog'),
        )

    #WEBSITE_CHOICES = (
    #    ('PER', 'Personal'),
    #    ('ORG', 'Organization'),
    #    ('FAC', 'Facebook'),
    #    ('TWI', 'Twitter'),
    #    ('GOO', 'Google'),
    #    ('YOU', 'Youtube'),
    #    ('SIN', 'Sina Weibo'),
    #    ('QZO', 'Qzone'),
    #    ('VIN', 'Vine'),
    #    ('INS', 'Instagram'),
    #    ('VK', 'VK'),
    #    ('LIN', 'Linkedin'),
    #    ('REN', 'Renren'),
    #    ('PIN', 'Pinterest'),
    #    ('TUM', 'Tumblr'),
    #    ('FRI', 'Friendster'),
    #    ('FOU', 'Foursquare'),
    #    ('PAT', 'Path'),
    #    ('MYS', 'Myspace'),
    #    ('TUE', 'Tuenti'),
    #    ('WOR', 'Wordpress'),
    #    ('BLO', 'Blogger'),
    #    ('SQU', 'Squarepage'),
    #    ('MED', 'Medium'),
    #    ('HUB', 'Hubpages'),
    #    ('JUM', 'Jumla'),
    #    ('LIV', 'Live Journal'),
    #    ('QUO', 'Quora'),
    #    ('TYP', 'Typepad'),
    #    ('WEE', 'Weebly'),
    #    ('DRU', 'Drupal'),
    #    ('SQU', 'Squidoo'),
    #    ('POS', 'Postachio'),
    #    ('FBN', 'Facebook Notes'),
    #    ('SVT', 'Svtle'),
    #    ('SET', 'Sett'),
    #    ('GHO', 'Ghost'),
    #    ('PHA', 'Posthaven'),
    #    ('PRS', 'Posterous'),
    #    ('BLG', 'Blog'),
    #    ('ZOO', 'Zoomshare'),
    #    ('XAN', 'Xanga'),
    #     )
    
    link = models.URLField(_('social link'), max_length = 300, 
        help_text = _('url corresponding to a social link'))
    #website = models.CharField(_('name of website'), max_length = 3, 
    #    choices = WEBSITE_CHOICES, help_text = _('the website corresponding \
    #    to the link. The backend automatically tries to identify the website \
    #    corresponding to the link and returns the identity of the website \
    #    as a three character code. When this identification fails, PER is \
    #    returned'))
    link_type = models.CharField(_('this link goes to'), max_length =3,
        choices = LINK_TYPE_CHOICES, help_text = _('denotes the type of social \
        link. fac means facebook, twi means twitter, blo means blog, quo means quora \
        lin means linkedin, wik means wikipedia'))

    #def get_website_type(self):
    #    return 'PER'

    class Meta:
        abstract = True