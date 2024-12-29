---
layout: page
title: Joshua Fox<br> יהושע פוקס
subtitle:
css: index_page
use-site-title: true
---

<div id="central-indexpage">
{% for link in site.navbar-links %}
  <div class="link-group">
  {% if link[1].first %}
    {% for childlink in link[1] %}
      {% for linkparts in childlink %}
        {% include navbarlink.html link=linkparts %}
      {% endfor %}
      <span class="link-separator">•</span>
    {% endfor %}
  {% else %}
    {% include navbarlink.html link=link %}
  {% endif %}
  </div>
{% endfor %}
</div>