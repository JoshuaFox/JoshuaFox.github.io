---
layout: page
title: Joshua  Fox<br> יהושע פוקס
subtitle:
css: index_page
use-site-title: true
---
<div id="central-indexpage">
 {% for link in site.navbar-links %}
  {% if link[1].first %}
      {% for childlink in link[1] %}
        {% for linkparts in childlink %}
          {% include navbarlink.html link=linkparts %} 
        {% endfor %}
        {%- if forloop.last == false -%}&nbsp;• {%- endif -%}
      {% endfor %}
  {%- else -%} •
    {%- include navbarlink.html link=link -%}
 <br/>  
  {%- endif -%}
{% endfor %}
</div>
 