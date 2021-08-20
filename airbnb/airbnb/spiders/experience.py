# -*- coding: utf-8 -*-
import scrapy
import json

class ExperienceSpider(scrapy.Spider):
    name = 'experience'
    allowed_domains = ['www.airbnb.com']
    
    def start_requests(self):
        yield scrapy.Request(url='https://www.airbnb.com/api/v2/explore_tabs?_format=for_explore_search_web&auto_ib=false&click_referer=t%3ASEE_ALL%7Csid%3A6909dfdb-1411-46c3-b0df-7d56975c34d0%7Cst%3AEXPERIENCES_FEATURED&client_session_id=6dcf83a9-7f75-45ce-b154-d512ff41cb3f&currency=USD&current_tab_id=experience_tab&experiences_per_grid=20&federated_search_session_id=f80f82d4-ebfb-4162-8191-49c4eea0b94e&fetch_filters=true&guidebooks_per_grid=20&has_zero_guest_treatment=true&hide_dates_and_guests_filters=false&is_guided_search=true&is_new_cards_experiment=true&is_standard_search=true&items_offset=18&items_per_grid=20&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=en&map_toggle=false&metadata_only=false&place_id=ChIJOwg_06VPwokRYv534QaPC8g&query=New%20York&query_understanding_enabled=true&refinement_paths%5B%5D=%2Fexperiences%2Fsection%2FPAGINATED_EXPERIENCES&satori_config_token=EhIbAYgac2F0b3JpX2NsaWVudF9sb2dnaW5nX3Rlc3QJdHJlYXRtZW50AA&satori_version=1.1.1&screen_height=625&screen_size=small&screen_width=619&search_type=pagination&selected_tab_id=experience_tab&show_groupings=true&supports_for_you_v3=true&timezone_offset=360&version=1.7.3', callback=self.parse_id)
    
    def parse_id(self, response):
        data =json.loads(response.body)
        with open('sample.json', 'w') as file:
            file.write(json.dumps(data))

    def parse(self, response):
        pass
