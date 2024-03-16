from bs4 import BeautifulSoup

html = """<li class="col-12 col-sm-6 col-md-4">
                        <div class="teaser-product-info possibility--true">
               <a class="teaser-product-info__link" target="" href="https://kunststoffplatten.at/plexiglas/bearbeiten/biegen/"> 								<div class="teaser-product-info__groups">
                  <div class="teaser-product-info__group">
                    <div class="teaser-product-info__image">
                                            <img width="150" height="150" src="https://kunststoffplatten.at/wp-content/uploads/2021/11/Kunststoff-biegen-warm-150x150.png" class="attachment-thumbnail size-thumbnail" alt="" decoding="async" loading="lazy" srcset="https://kunststoffplatten.at/wp-content/uploads/2021/11/Kunststoff-biegen-warm-150x150.png 150w, https://kunststoffplatten.at/wp-content/uploads/2021/11/Kunststoff-biegen-warm-300x300.png 300w, https://kunststoffplatten.at/wp-content/uploads/2021/11/Kunststoff-biegen-warm-45x45.png 45w, https://kunststoffplatten.at/wp-content/uploads/2021/11/Kunststoff-biegen-warm-100x100.png 100w, https://kunststoffplatten.at/wp-content/uploads/2021/11/Kunststoff-biegen-warm-120x120.png 120w, https://kunststoffplatten.at/wp-content/uploads/2021/11/Kunststoff-biegen-warm.png 320w" sizes="(max-width: 150px) 100vw, 150px">
                    </div>
                  </div>
                  <div class="teaser-product-info__group">
                    <div class="teaser-product-info__inner">
                      <div class="teaser-product-info__title">Biegen (warm)</div>
                                              <div class="teaser-product-info__read-more">
                          <i class="teaser-product-info__icon icon icon-chevron-right" aria-hidden="true"></i>
                          <span>Weitere Informationen</span>
                        </div>
                                          </div>
                  </div>
                </div>
               </a> 						</div>
          </li>"""

soup = BeautifulSoup(html, 'html.parser')

# Extract the aria-hidden value
aria_hidden_value = soup.select_one('i.icon')['aria-hidden']
print("aria-hidden value:", aria_hidden_value)

# Extract the title
title = soup.select_one('div.teaser-product-info__title').text
print("Title:", title)
