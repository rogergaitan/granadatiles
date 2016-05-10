from core.dtos import BaseContentDto, BaseCatalogOrderDto, BaseGalleryNavImageDto
from apps.news.dtos import SectionFeaturedArticleDto


class TestimonyDto(BaseContentDto):

    def __init__(self, testimony, language=None):
        super().__init__(testimony, language)
        if language:
            self.subtitle = testimony.get_subtitle(language)
        else:
            self.subtitle = testimony.get_subtitle()


class SectionCoverDto(object):
    featuredArticle = None
    articles = None

    def __init__(self, section_image, language):
        self.image = section_image.image.url
        self.designer = section_image.designer
        self.photographer = section_image.photographer
        self.shopCustomTilesUrl = section_image.tile.design.group.get_absolute_url(language) if section_image.tile else ''


class FeaturedVideoDto(BaseCatalogOrderDto):

    def __init__(self, featured_video, language=None):
        super().__init__(featured_video, language)
        self.video = featured_video.video

class IndexNavigationDto(BaseGalleryNavImageDto):

    def __init__(self, baseGalleryNavImageModel, language = None):
        super().__init__(baseGalleryNavImageModel, language)
        self.actionName = baseGalleryNavImageModel.get_action_name(language=language)
        if language == 'es' and baseGalleryNavImageModel.link_es:
            self.link = baseGalleryNavImageModel.link_es

class FlatPageDto(object):

    def __init__(self, flatpage, language):
        self.title = flatpage.get_title(language=language)
        self.description = flatpage.get_content(language=language)
        self.menu = flatpage.menu

class FlatPageCoverDto(object):

    def __init__(self, flatPage):
        self.image = flatPage.cover.url if flatPage.cover else ''

class FlatPageMenuDto(object):

    def __init__(self, flatPage, language):
        if(language is None):
            language='en'
        self.title = flatPage.get_menu(language=language)
        self.url = flatPage.get_url(language)

class CollectionContentDto(object):

    def __init__(self, content, language):
        self.title = content.get_title(language=language)
        self.description = content.get_content(language=language)
        self.collectionId = content.collection.id
        self.url = content.get_url(language)
