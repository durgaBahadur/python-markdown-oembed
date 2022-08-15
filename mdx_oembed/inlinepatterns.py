# -*- coding: utf-8 -*-
import logging
from markdown.inlinepatterns import Pattern
import oembed


LOG = logging.getLogger(__name__)


OEMBED_LINK_RE = r'\!\[([^\]]*)\]\(((?:https?:)?//[^\)]*)' \
                 r'(?<!png)(?<!jpg)(?<!jpeg)(?<!gif)\)'


class OEmbedLinkPattern(Pattern):

    def __init__(self, pattern, markdown_instance=None, oembed_consumer=None):
        Pattern.__init__(self, pattern, markdown_instance)
        self.consumer = oembed_consumer

    def handleMatch(self, match):
        html = self.get_oembed_html_for_match(match)
        LOG.info(html)
        if html is None:
            return None
        else:
            html = "<figure class=\"oembed\">%s</figure>" % html
            placeholder = self.markdown.htmlStash.store(html)
            return placeholder

    def get_oembed_html_for_match(self, match):
        url = match.group(3).strip()
        LOG.info(url)
        try:
            response = self.consumer.embed(url)
        except oembed.OEmbedNoEndpoint:
            LOG.error("No OEmbed Endpoint")
            return None
        except Exception as e:
            LOG.error(e)
            return None
        else:
            return response['html']
