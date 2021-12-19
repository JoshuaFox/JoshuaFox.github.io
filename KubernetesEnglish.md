---
layout: page
title: "Kubernetes in Plain English"
subtitle:
tags: [ yiddish]
css: yiddish
---

<html>
<head>
<meta content="text/html; charset=UTF-8" http-equiv="content-type">
<style type="text/css">.lst-kix_qghhohyfbmul-2>li:before{content:"\0025a0  "}ul.lst-kix_szyv8lazwfte-2{list-style-type:none}ul.lst-kix_szyv8lazwfte-3{list-style-type:none}.lst-kix_qghhohyfbmul-1>li:before{content:"\0025cb  "}.lst-kix_qghhohyfbmul-3>li:before{content:"\0025cf  "}ul.lst-kix_szyv8lazwfte-0{list-style-type:none}ul.lst-kix_szyv8lazwfte-1{list-style-type:none}.lst-kix_qghhohyfbmul-0>li:before{content:"\0025cf  "}.lst-kix_qghhohyfbmul-4>li:before{content:"\0025cb  "}ul.lst-kix_szyv8lazwfte-6{list-style-type:none}ul.lst-kix_szyv8lazwfte-7{list-style-type:none}ul.lst-kix_szyv8lazwfte-4{list-style-type:none}ul.lst-kix_szyv8lazwfte-5{list-style-type:none}.lst-kix_qghhohyfbmul-6>li:before{content:"\0025cf  "}.lst-kix_qghhohyfbmul-5>li:before{content:"\0025a0  "}.lst-kix_qghhohyfbmul-7>li:before{content:"\0025cb  "}ul.lst-kix_szyv8lazwfte-8{list-style-type:none}.lst-kix_uzlu6ke0i96j-4>li{counter-increment:lst-ctn-kix_uzlu6ke0i96j-4}ul.lst-kix_ihfuwi4lpncg-5{list-style-type:none}.lst-kix_szyv8lazwfte-0>li:before{content:"\0025cf  "}ul.lst-kix_ihfuwi4lpncg-6{list-style-type:none}.lst-kix_dsfec7td0jft-1>li:before{content:"\0025cb  "}.lst-kix_dsfec7td0jft-2>li:before{content:"\0025a0  "}ul.lst-kix_ihfuwi4lpncg-3{list-style-type:none}ul.lst-kix_ihfuwi4lpncg-4{list-style-type:none}ul.lst-kix_ihfuwi4lpncg-1{list-style-type:none}ol.lst-kix_uzlu6ke0i96j-1.start{counter-reset:lst-ctn-kix_uzlu6ke0i96j-1 0}.lst-kix_szyv8lazwfte-2>li:before{content:"\0025a0  "}ul.lst-kix_ihfuwi4lpncg-2{list-style-type:none}.lst-kix_szyv8lazwfte-1>li:before{content:"\0025cb  "}ul.lst-kix_ihfuwi4lpncg-0{list-style-type:none}.lst-kix_szyv8lazwfte-4>li:before{content:"\0025cb  "}ul.lst-kix_dsfec7td0jft-0{list-style-type:none}ul.lst-kix_dsfec7td0jft-2{list-style-type:none}ul.lst-kix_dsfec7td0jft-1{list-style-type:none}ul.lst-kix_dsfec7td0jft-4{list-style-type:none}.lst-kix_dsfec7td0jft-0>li:before{content:"\0025cf  "}ul.lst-kix_dsfec7td0jft-3{list-style-type:none}.lst-kix_szyv8lazwfte-3>li:before{content:"\0025cf  "}ul.lst-kix_dsfec7td0jft-6{list-style-type:none}ul.lst-kix_dsfec7td0jft-5{list-style-type:none}ul.lst-kix_dsfec7td0jft-8{list-style-type:none}.lst-kix_uzlu6ke0i96j-2>li{counter-increment:lst-ctn-kix_uzlu6ke0i96j-2}ul.lst-kix_dsfec7td0jft-7{list-style-type:none}ul.lst-kix_prhopwzg51ya-4{list-style-type:none}ul.lst-kix_prhopwzg51ya-5{list-style-type:none}ul.lst-kix_prhopwzg51ya-6{list-style-type:none}ul.lst-kix_prhopwzg51ya-7{list-style-type:none}ul.lst-kix_prhopwzg51ya-0{list-style-type:none}.lst-kix_qghhohyfbmul-8>li:before{content:"\0025a0  "}ul.lst-kix_prhopwzg51ya-1{list-style-type:none}ul.lst-kix_prhopwzg51ya-2{list-style-type:none}ul.lst-kix_prhopwzg51ya-3{list-style-type:none}ul.lst-kix_prhopwzg51ya-8{list-style-type:none}.lst-kix_prhopwzg51ya-2>li:before{content:"\0025a0  "}.lst-kix_g0gsqjenso1g-2>li:before{content:"\0025a0  "}.lst-kix_g0gsqjenso1g-3>li:before{content:"\0025cf  "}.lst-kix_prhopwzg51ya-1>li:before{content:"\0025cb  "}.lst-kix_prhopwzg51ya-3>li:before{content:"\0025cf  "}ul.lst-kix_a3bncohmjifs-5{list-style-type:none}.lst-kix_prhopwzg51ya-6>li:before{content:"\0025cf  "}ul.lst-kix_a3bncohmjifs-4{list-style-type:none}ul.lst-kix_g0gsqjenso1g-8{list-style-type:none}ul.lst-kix_a3bncohmjifs-3{list-style-type:none}.lst-kix_prhopwzg51ya-5>li:before{content:"\0025a0  "}ul.lst-kix_a3bncohmjifs-2{list-style-type:none}ul.lst-kix_a3bncohmjifs-1{list-style-type:none}.lst-kix_prhopwzg51ya-4>li:before{content:"\0025cb  "}ul.lst-kix_a3bncohmjifs-0{list-style-type:none}.lst-kix_g0gsqjenso1g-0>li:before{content:"\0025cf  "}.lst-kix_g0gsqjenso1g-1>li:before{content:"\0025cb  "}ul.lst-kix_g0gsqjenso1g-1{list-style-type:none}ul.lst-kix_g0gsqjenso1g-0{list-style-type:none}ul.lst-kix_g0gsqjenso1g-3{list-style-type:none}ul.lst-kix_g0gsqjenso1g-2{list-style-type:none}ul.lst-kix_g0gsqjenso1g-5{list-style-type:none}ul.lst-kix_g0gsqjenso1g-4{list-style-type:none}ul.lst-kix_g0gsqjenso1g-7{list-style-type:none}ol.lst-kix_uzlu6ke0i96j-6.start{counter-reset:lst-ctn-kix_uzlu6ke0i96j-6 0}.lst-kix_uzlu6ke0i96j-6>li{counter-increment:lst-ctn-kix_uzlu6ke0i96j-6}ul.lst-kix_g0gsqjenso1g-6{list-style-type:none}.lst-kix_prhopwzg51ya-0>li:before{content:"\0025cf  "}.lst-kix_uzlu6ke0i96j-0>li{counter-increment:lst-ctn-kix_uzlu6ke0i96j-0}ol.lst-kix_uzlu6ke0i96j-0{list-style-type:none}ol.lst-kix_uzlu6ke0i96j-1{list-style-type:none}ol.lst-kix_uzlu6ke0i96j-2{list-style-type:none}ol.lst-kix_uzlu6ke0i96j-3{list-style-type:none}ol.lst-kix_uzlu6ke0i96j-4{list-style-type:none}.lst-kix_dsfec7td0jft-5>li:before{content:"\0025a0  "}.lst-kix_dsfec7td0jft-3>li:before{content:"\0025cf  "}.lst-kix_dsfec7td0jft-4>li:before{content:"\0025cb  "}.lst-kix_ihfuwi4lpncg-4>li:before{content:"\0025cb  "}ul.lst-kix_39p98texbnc0-6{list-style-type:none}ul.lst-kix_39p98texbnc0-7{list-style-type:none}ul.lst-kix_39p98texbnc0-8{list-style-type:none}.lst-kix_ihfuwi4lpncg-2>li:before{content:"\0025a0  "}ul.lst-kix_39p98texbnc0-2{list-style-type:none}ul.lst-kix_a3bncohmjifs-8{list-style-type:none}ul.lst-kix_39p98texbnc0-3{list-style-type:none}ul.lst-kix_a3bncohmjifs-7{list-style-type:none}.lst-kix_ihfuwi4lpncg-3>li:before{content:"\0025cf  "}ul.lst-kix_39p98texbnc0-4{list-style-type:none}ul.lst-kix_a3bncohmjifs-6{list-style-type:none}ul.lst-kix_39p98texbnc0-5{list-style-type:none}.lst-kix_ihfuwi4lpncg-0>li:before{content:"\0025cf  "}ol.lst-kix_uzlu6ke0i96j-5{list-style-type:none}ol.lst-kix_uzlu6ke0i96j-6{list-style-type:none}.lst-kix_dsfec7td0jft-6>li:before{content:"\0025cf  "}.lst-kix_prhopwzg51ya-7>li:before{content:"\0025cb  "}ul.lst-kix_39p98texbnc0-0{list-style-type:none}ol.lst-kix_uzlu6ke0i96j-7{list-style-type:none}ul.lst-kix_39p98texbnc0-1{list-style-type:none}ol.lst-kix_uzlu6ke0i96j-8{list-style-type:none}.lst-kix_prhopwzg51ya-8>li:before{content:"\0025a0  "}.lst-kix_dsfec7td0jft-7>li:before{content:"\0025cb  "}.lst-kix_dsfec7td0jft-8>li:before{content:"\0025a0  "}.lst-kix_ihfuwi4lpncg-1>li:before{content:"\0025cb  "}ol.lst-kix_uzlu6ke0i96j-7.start{counter-reset:lst-ctn-kix_uzlu6ke0i96j-7 0}.lst-kix_d7s5hs4d40i8-5>li:before{content:"\0025a0  "}.lst-kix_1l7d0zqaor0a-0>li:before{content:"\0025cf  "}.lst-kix_d7s5hs4d40i8-3>li:before{content:"\0025cf  "}.lst-kix_d7s5hs4d40i8-7>li:before{content:"\0025cb  "}.lst-kix_1l7d0zqaor0a-2>li:before{content:"\0025a0  "}ul.lst-kix_gj9eps2krm16-7{list-style-type:none}.lst-kix_d7s5hs4d40i8-1>li:before{content:"\0025cb  "}ul.lst-kix_gj9eps2krm16-6{list-style-type:none}ul.lst-kix_gj9eps2krm16-8{list-style-type:none}.lst-kix_ihfuwi4lpncg-5>li:before{content:"\0025a0  "}.lst-kix_dutf5eqbmav9-5>li:before{content:"-  "}.lst-kix_1l7d0zqaor0a-8>li:before{content:"\0025a0  "}ul.lst-kix_gj9eps2krm16-1{list-style-type:none}ul.lst-kix_gj9eps2krm16-0{list-style-type:none}ul.lst-kix_gj9eps2krm16-3{list-style-type:none}.lst-kix_1l7d0zqaor0a-6>li:before{content:"\0025cf  "}ul.lst-kix_gj9eps2krm16-2{list-style-type:none}.lst-kix_dutf5eqbmav9-3>li:before{content:"-  "}ul.lst-kix_gj9eps2krm16-5{list-style-type:none}.lst-kix_ihfuwi4lpncg-7>li:before{content:"\0025cb  "}.lst-kix_d162uvvcvhcs-1>li:before{content:"\0025cb  "}ul.lst-kix_gj9eps2krm16-4{list-style-type:none}.lst-kix_1l7d0zqaor0a-4>li:before{content:"\0025cb  "}.lst-kix_dutf5eqbmav9-1>li:before{content:"-  "}.lst-kix_plxzfrrogkn5-7>li:before{content:"-  "}.lst-kix_plxzfrrogkn5-5>li:before{content:"-  "}ol.lst-kix_uzlu6ke0i96j-5.start{counter-reset:lst-ctn-kix_uzlu6ke0i96j-5 0}.lst-kix_r4qtpgpmprer-8>li:before{content:"\0025a0  "}ol.lst-kix_uzlu6ke0i96j-2.start{counter-reset:lst-ctn-kix_uzlu6ke0i96j-2 0}.lst-kix_g0gsqjenso1g-5>li:before{content:"\0025a0  "}.lst-kix_uzlu6ke0i96j-1>li:before{content:"" counter(lst-ctn-kix_uzlu6ke0i96j-1,lower-latin) ". "}.lst-kix_g0gsqjenso1g-7>li:before{content:"\0025cb  "}.lst-kix_uzlu6ke0i96j-5>li:before{content:"" counter(lst-ctn-kix_uzlu6ke0i96j-5,lower-roman) ". "}.lst-kix_uzlu6ke0i96j-3>li:before{content:"" counter(lst-ctn-kix_uzlu6ke0i96j-3,decimal) ". "}.lst-kix_gj9eps2krm16-3>li:before{content:"\0025cf  "}.lst-kix_plxzfrrogkn5-1>li:before{content:"-  "}.lst-kix_plxzfrrogkn5-3>li:before{content:"-  "}.lst-kix_uzlu6ke0i96j-7>li:before{content:"" counter(lst-ctn-kix_uzlu6ke0i96j-7,lower-latin) ". "}.lst-kix_gj9eps2krm16-1>li:before{content:"\0025cb  "}.lst-kix_d162uvvcvhcs-7>li:before{content:"\0025cb  "}.lst-kix_szyv8lazwfte-8>li:before{content:"\0025a0  "}ol.lst-kix_uzlu6ke0i96j-3.start{counter-reset:lst-ctn-kix_uzlu6ke0i96j-3 0}.lst-kix_d162uvvcvhcs-5>li:before{content:"\0025a0  "}.lst-kix_szyv8lazwfte-6>li:before{content:"\0025cf  "}ul.lst-kix_ihfuwi4lpncg-7{list-style-type:none}.lst-kix_d162uvvcvhcs-3>li:before{content:"\0025cf  "}ul.lst-kix_ihfuwi4lpncg-8{list-style-type:none}ul.lst-kix_sjpvbx9lpat-2{list-style-type:none}ul.lst-kix_sjpvbx9lpat-3{list-style-type:none}ul.lst-kix_sjpvbx9lpat-0{list-style-type:none}ul.lst-kix_sjpvbx9lpat-1{list-style-type:none}ul.lst-kix_sjpvbx9lpat-6{list-style-type:none}ul.lst-kix_sjpvbx9lpat-7{list-style-type:none}ul.lst-kix_sjpvbx9lpat-4{list-style-type:none}ul.lst-kix_sjpvbx9lpat-5{list-style-type:none}ul.lst-kix_sjpvbx9lpat-8{list-style-type:none}.lst-kix_pug5pytkp60-0>li:before{content:"\0025cf  "}.lst-kix_pug5pytkp60-1>li:before{content:"\0025cb  "}ol.lst-kix_uzlu6ke0i96j-4.start{counter-reset:lst-ctn-kix_uzlu6ke0i96j-4 0}.lst-kix_pug5pytkp60-2>li:before{content:"\0025a0  "}.lst-kix_pug5pytkp60-5>li:before{content:"\0025a0  "}.lst-kix_39p98texbnc0-8>li:before{content:"-  "}.lst-kix_pug5pytkp60-3>li:before{content:"\0025cf  "}.lst-kix_39p98texbnc0-6>li:before{content:"-  "}.lst-kix_39p98texbnc0-7>li:before{content:"-  "}.lst-kix_pug5pytkp60-4>li:before{content:"\0025cb  "}.lst-kix_a3bncohmjifs-3>li:before{content:"\0025cf  "}.lst-kix_a3bncohmjifs-1>li:before{content:"\0025cb  "}.lst-kix_a3bncohmjifs-2>li:before{content:"\0025a0  "}.lst-kix_pug5pytkp60-6>li:before{content:"\0025cf  "}.lst-kix_pug5pytkp60-7>li:before{content:"\0025cb  "}.lst-kix_uzlu6ke0i96j-3>li{counter-increment:lst-ctn-kix_uzlu6ke0i96j-3}.lst-kix_a3bncohmjifs-0>li:before{content:"\0025cf  "}.lst-kix_pug5pytkp60-8>li:before{content:"\0025a0  "}.lst-kix_uzlu6ke0i96j-5>li{counter-increment:lst-ctn-kix_uzlu6ke0i96j-5}.lst-kix_gj9eps2krm16-5>li:before{content:"\0025a0  "}.lst-kix_gj9eps2krm16-6>li:before{content:"\0025cf  "}.lst-kix_gj9eps2krm16-7>li:before{content:"\0025cb  "}.lst-kix_xlnhit7wndh-0>li:before{content:"\0025cf  "}.lst-kix_xlnhit7wndh-1>li:before{content:"\0025cb  "}.lst-kix_gj9eps2krm16-8>li:before{content:"\0025a0  "}ul.lst-kix_pug5pytkp60-1{list-style-type:none}ul.lst-kix_pug5pytkp60-0{list-style-type:none}ul.lst-kix_pug5pytkp60-3{list-style-type:none}ul.lst-kix_pug5pytkp60-2{list-style-type:none}.lst-kix_xlnhit7wndh-4>li:before{content:"\0025cb  "}.lst-kix_xlnhit7wndh-5>li:before{content:"\0025a0  "}ul.lst-kix_pug5pytkp60-5{list-style-type:none}.lst-kix_sjpvbx9lpat-1>li:before{content:"-  "}ul.lst-kix_pug5pytkp60-4{list-style-type:none}ul.lst-kix_pug5pytkp60-7{list-style-type:none}ul.lst-kix_pug5pytkp60-6{list-style-type:none}.lst-kix_xlnhit7wndh-2>li:before{content:"\0025a0  "}.lst-kix_xlnhit7wndh-3>li:before{content:"\0025cf  "}.lst-kix_xlnhit7wndh-6>li:before{content:"\0025cf  "}.lst-kix_xlnhit7wndh-7>li:before{content:"\0025cb  "}.lst-kix_sjpvbx9lpat-2>li:before{content:"-  "}ul.lst-kix_pug5pytkp60-8{list-style-type:none}ul.lst-kix_xlnhit7wndh-8{list-style-type:none}ul.lst-kix_xlnhit7wndh-7{list-style-type:none}ul.lst-kix_xlnhit7wndh-6{list-style-type:none}ul.lst-kix_xlnhit7wndh-5{list-style-type:none}ul.lst-kix_xlnhit7wndh-4{list-style-type:none}ul.lst-kix_xlnhit7wndh-3{list-style-type:none}ul.lst-kix_xlnhit7wndh-2{list-style-type:none}.lst-kix_r4qtpgpmprer-7>li:before{content:"\0025cb  "}ul.lst-kix_xlnhit7wndh-1{list-style-type:none}.lst-kix_sjpvbx9lpat-0>li:before{content:"-  "}ul.lst-kix_xlnhit7wndh-0{list-style-type:none}.lst-kix_sjpvbx9lpat-7>li:before{content:"-  "}ul.lst-kix_r4qtpgpmprer-0{list-style-type:none}.lst-kix_r4qtpgpmprer-5>li:before{content:"\0025a0  "}.lst-kix_r4qtpgpmprer-6>li:before{content:"\0025cf  "}.lst-kix_r4qtpgpmprer-4>li:before{content:"\0025cb  "}.lst-kix_sjpvbx9lpat-6>li:before{content:"-  "}ul.lst-kix_r4qtpgpmprer-7{list-style-type:none}.lst-kix_xlnhit7wndh-8>li:before{content:"\0025a0  "}.lst-kix_r4qtpgpmprer-1>li:before{content:"\0025cb  "}.lst-kix_r4qtpgpmprer-2>li:before{content:"\0025a0  "}ul.lst-kix_r4qtpgpmprer-8{list-style-type:none}ul.lst-kix_r4qtpgpmprer-5{list-style-type:none}.lst-kix_sjpvbx9lpat-3>li:before{content:"-  "}.lst-kix_sjpvbx9lpat-5>li:before{content:"-  "}ul.lst-kix_r4qtpgpmprer-6{list-style-type:none}ul.lst-kix_r4qtpgpmprer-3{list-style-type:none}.lst-kix_r4qtpgpmprer-3>li:before{content:"\0025cf  "}ul.lst-kix_r4qtpgpmprer-4{list-style-type:none}ul.lst-kix_r4qtpgpmprer-1{list-style-type:none}.lst-kix_sjpvbx9lpat-4>li:before{content:"-  "}ul.lst-kix_r4qtpgpmprer-2{list-style-type:none}.lst-kix_r4qtpgpmprer-0>li:before{content:"\0025cf  "}.lst-kix_39p98texbnc0-0>li:before{content:"-  "}.lst-kix_a3bncohmjifs-4>li:before{content:"\0025cb  "}.lst-kix_sjpvbx9lpat-8>li:before{content:"-  "}.lst-kix_39p98texbnc0-4>li:before{content:"-  "}.lst-kix_39p98texbnc0-5>li:before{content:"-  "}.lst-kix_dutf5eqbmav9-6>li:before{content:"-  "}.lst-kix_a3bncohmjifs-5>li:before{content:"\0025a0  "}.lst-kix_a3bncohmjifs-6>li:before{content:"\0025cf  "}.lst-kix_dutf5eqbmav9-7>li:before{content:"-  "}.lst-kix_a3bncohmjifs-7>li:before{content:"\0025cb  "}.lst-kix_39p98texbnc0-1>li:before{content:"-  "}.lst-kix_dutf5eqbmav9-8>li:before{content:"-  "}.lst-kix_39p98texbnc0-2>li:before{content:"-  "}.lst-kix_39p98texbnc0-3>li:before{content:"-  "}.lst-kix_a3bncohmjifs-8>li:before{content:"\0025a0  "}ul.lst-kix_d7s5hs4d40i8-6{list-style-type:none}ul.lst-kix_d7s5hs4d40i8-7{list-style-type:none}.lst-kix_d7s5hs4d40i8-4>li:before{content:"\0025cb  "}.lst-kix_d7s5hs4d40i8-6>li:before{content:"\0025cf  "}ul.lst-kix_d7s5hs4d40i8-8{list-style-type:none}.lst-kix_dutf5eqbmav9-0>li:before{content:"-  "}.lst-kix_1l7d0zqaor0a-3>li:before{content:"\0025cf  "}.lst-kix_d7s5hs4d40i8-0>li:before{content:"\0025cf  "}.lst-kix_d7s5hs4d40i8-2>li:before{content:"\0025a0  "}.lst-kix_d7s5hs4d40i8-8>li:before{content:"\0025a0  "}ul.lst-kix_dutf5eqbmav9-6{list-style-type:none}ul.lst-kix_dutf5eqbmav9-7{list-style-type:none}ul.lst-kix_dutf5eqbmav9-8{list-style-type:none}.lst-kix_1l7d0zqaor0a-1>li:before{content:"\0025cb  "}ul.lst-kix_d162uvvcvhcs-6{list-style-type:none}ul.lst-kix_plxzfrrogkn5-0{list-style-type:none}ul.lst-kix_d162uvvcvhcs-7{list-style-type:none}ul.lst-kix_d162uvvcvhcs-4{list-style-type:none}ul.lst-kix_plxzfrrogkn5-2{list-style-type:none}ol.lst-kix_uzlu6ke0i96j-0.start{counter-reset:lst-ctn-kix_uzlu6ke0i96j-0 0}.lst-kix_d162uvvcvhcs-0>li:before{content:"\0025cf  "}ul.lst-kix_d162uvvcvhcs-5{list-style-type:none}.lst-kix_dutf5eqbmav9-4>li:before{content:"-  "}ul.lst-kix_plxzfrrogkn5-1{list-style-type:none}ul.lst-kix_d162uvvcvhcs-2{list-style-type:none}.lst-kix_ihfuwi4lpncg-6>li:before{content:"\0025cf  "}ul.lst-kix_plxzfrrogkn5-4{list-style-type:none}ul.lst-kix_d162uvvcvhcs-3{list-style-type:none}ul.lst-kix_plxzfrrogkn5-3{list-style-type:none}ul.lst-kix_d162uvvcvhcs-0{list-style-type:none}.lst-kix_1l7d0zqaor0a-7>li:before{content:"\0025cb  "}ul.lst-kix_plxzfrrogkn5-6{list-style-type:none}ul.lst-kix_d162uvvcvhcs-1{list-style-type:none}ul.lst-kix_plxzfrrogkn5-5{list-style-type:none}.lst-kix_dutf5eqbmav9-2>li:before{content:"-  "}.lst-kix_ihfuwi4lpncg-8>li:before{content:"\0025a0  "}ul.lst-kix_plxzfrrogkn5-8{list-style-type:none}ol.lst-kix_uzlu6ke0i96j-8.start{counter-reset:lst-ctn-kix_uzlu6ke0i96j-8 0}ul.lst-kix_plxzfrrogkn5-7{list-style-type:none}.lst-kix_1l7d0zqaor0a-5>li:before{content:"\0025a0  "}.lst-kix_plxzfrrogkn5-4>li:before{content:"-  "}.lst-kix_plxzfrrogkn5-8>li:before{content:"-  "}ul.lst-kix_d162uvvcvhcs-8{list-style-type:none}.lst-kix_plxzfrrogkn5-6>li:before{content:"-  "}ul.lst-kix_dutf5eqbmav9-2{list-style-type:none}ul.lst-kix_qghhohyfbmul-5{list-style-type:none}ul.lst-kix_1l7d0zqaor0a-1{list-style-type:none}ul.lst-kix_dutf5eqbmav9-3{list-style-type:none}ul.lst-kix_qghhohyfbmul-6{list-style-type:none}ul.lst-kix_1l7d0zqaor0a-2{list-style-type:none}ul.lst-kix_dutf5eqbmav9-4{list-style-type:none}ul.lst-kix_qghhohyfbmul-3{list-style-type:none}ul.lst-kix_dutf5eqbmav9-5{list-style-type:none}ul.lst-kix_qghhohyfbmul-4{list-style-type:none}ul.lst-kix_1l7d0zqaor0a-0{list-style-type:none}ul.lst-kix_dutf5eqbmav9-0{list-style-type:none}ul.lst-kix_qghhohyfbmul-7{list-style-type:none}ul.lst-kix_dutf5eqbmav9-1{list-style-type:none}ul.lst-kix_qghhohyfbmul-8{list-style-type:none}.lst-kix_g0gsqjenso1g-6>li:before{content:"\0025cf  "}ul.lst-kix_1l7d0zqaor0a-7{list-style-type:none}ul.lst-kix_1l7d0zqaor0a-8{list-style-type:none}ul.lst-kix_1l7d0zqaor0a-5{list-style-type:none}.lst-kix_g0gsqjenso1g-4>li:before{content:"\0025cb  "}ul.lst-kix_1l7d0zqaor0a-6{list-style-type:none}ul.lst-kix_1l7d0zqaor0a-3{list-style-type:none}.lst-kix_uzlu6ke0i96j-8>li{counter-increment:lst-ctn-kix_uzlu6ke0i96j-8}ul.lst-kix_1l7d0zqaor0a-4{list-style-type:none}.lst-kix_uzlu6ke0i96j-2>li:before{content:"" counter(lst-ctn-kix_uzlu6ke0i96j-2,lower-roman) ". "}.lst-kix_uzlu6ke0i96j-1>li{counter-increment:lst-ctn-kix_uzlu6ke0i96j-1}ul.lst-kix_qghhohyfbmul-1{list-style-type:none}.lst-kix_uzlu6ke0i96j-7>li{counter-increment:lst-ctn-kix_uzlu6ke0i96j-7}.lst-kix_g0gsqjenso1g-8>li:before{content:"\0025a0  "}ul.lst-kix_qghhohyfbmul-2{list-style-type:none}.lst-kix_uzlu6ke0i96j-4>li:before{content:"" counter(lst-ctn-kix_uzlu6ke0i96j-4,lower-latin) ". "}ul.lst-kix_qghhohyfbmul-0{list-style-type:none}.lst-kix_gj9eps2krm16-4>li:before{content:"\0025cb  "}.lst-kix_plxzfrrogkn5-0>li:before{content:"-  "}.lst-kix_uzlu6ke0i96j-6>li:before{content:"" counter(lst-ctn-kix_uzlu6ke0i96j-6,decimal) ". "}.lst-kix_gj9eps2krm16-2>li:before{content:"\0025a0  "}.lst-kix_gj9eps2krm16-0>li:before{content:"\0025cf  "}.lst-kix_uzlu6ke0i96j-8>li:before{content:"" counter(lst-ctn-kix_uzlu6ke0i96j-8,lower-roman) ". "}.lst-kix_plxzfrrogkn5-2>li:before{content:"-  "}.lst-kix_d162uvvcvhcs-6>li:before{content:"\0025cf  "}.lst-kix_d162uvvcvhcs-8>li:before{content:"\0025a0  "}.lst-kix_szyv8lazwfte-5>li:before{content:"\0025a0  "}.lst-kix_d162uvvcvhcs-2>li:before{content:"\0025a0  "}.lst-kix_d162uvvcvhcs-4>li:before{content:"\0025cb  "}li.li-bullet-0:before{margin-left:-18pt;white-space:nowrap;display:inline-block;min-width:18pt}.lst-kix_szyv8lazwfte-7>li:before{content:"\0025cb  "}ul.lst-kix_d7s5hs4d40i8-0{list-style-type:none}ul.lst-kix_d7s5hs4d40i8-1{list-style-type:none}ul.lst-kix_d7s5hs4d40i8-2{list-style-type:none}ul.lst-kix_d7s5hs4d40i8-3{list-style-type:none}.lst-kix_uzlu6ke0i96j-0>li:before{content:"" counter(lst-ctn-kix_uzlu6ke0i96j-0,decimal) ". "}ul.lst-kix_d7s5hs4d40i8-4{list-style-type:none}ul.lst-kix_d7s5hs4d40i8-5{list-style-type:none}ol{margin:0;padding:0}table td,table th{padding:0}.c15{border-right-style:solid;padding:5pt 5pt 5pt 5pt;border-bottom-color:#000000;border-top-width:1pt;border-right-width:1pt;border-left-color:#000000;vertical-align:top;border-right-color:#000000;border-left-width:1pt;border-top-style:solid;border-left-style:solid;border-bottom-width:1pt;width:451.3pt;border-top-color:#000000;border-bottom-style:solid}.c2{margin-left:72pt;padding-top:0pt;padding-left:0pt;padding-bottom:0pt;line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}.c3{-webkit-text-decoration-skip:none;color:#1155cc;font-weight:400;text-decoration:underline;text-decoration-skip-ink:none;font-size:14pt;font-family:"Times New Roman";font-style:italic}.c4{color:#000000;font-weight:400;text-decoration:none;vertical-align:baseline;font-size:11pt;font-family:"Arial";font-style:normal}.c14{padding-top:0pt;padding-bottom:3pt;line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}.c1{padding-top:0pt;padding-bottom:0pt;line-height:1.15;orphans:2;widows:2;text-align:left;height:11pt}.c11{padding-top:0pt;padding-bottom:0pt;line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}.c5{color:#000000;font-weight:400;text-decoration:none;vertical-align:baseline;font-size:14pt;font-family:"Times New Roman";font-style:normal}.c13{padding-top:0pt;padding-bottom:0pt;line-height:1.15;orphans:2;widows:2;text-align:left}.c22{font-weight:700;text-decoration:none;vertical-align:baseline;font-size:14pt;font-family:"Arial";font-style:normal}.c9{text-decoration:none;vertical-align:baseline;font-size:11pt;font-style:normal}.c28{border-spacing:0;border-collapse:collapse;margin-right:auto}.c25{-webkit-text-decoration-skip:none;color:#1155cc;text-decoration:underline;text-decoration-skip-ink:none}.c29{padding-top:0pt;padding-bottom:0pt;line-height:1.0;text-align:left}.c21{text-decoration:none;vertical-align:baseline;font-style:italic}.c17{font-size:14pt;font-family:"Times New Roman";font-weight:400}.c10{color:#1c4587;font-weight:400;font-family:"Arial"}.c27{background-color:#ffffff;max-width:451.3pt;padding:72pt 72pt 72pt 72pt}.c0{font-family:"Courier New";color:#000000;font-weight:400}.c19{margin-left:36pt;padding-left:0pt}.c30{font-family:"Courier New";font-weight:400}.c7{padding:0;margin:0}.c8{color:inherit;text-decoration:inherit}.c16{margin-right:36pt}.c12{font-size:8pt}.c20{margin-left:36pt}.c6{color:#000000}.c18{margin-right:72pt}.c24{height:0pt}.c23{page-break-after:avoid}.c26{height:11pt}.title{padding-top:0pt;color:#000000;font-weight:700;font-size:14pt;padding-bottom:3pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}.subtitle{padding-top:0pt;color:#666666;font-size:15pt;padding-bottom:16pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}li{color:#000000;font-size:11pt;font-family:"Arial"}p{margin:0;color:#000000;font-size:11pt;font-family:"Arial"}h1{padding-top:20pt;color:#000000;font-size:20pt;padding-bottom:6pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h2{padding-top:18pt;color:#000000;font-size:16pt;padding-bottom:6pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h3{padding-top:0pt;color:#1c4587;font-size:11pt;padding-bottom:0pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h4{padding-top:14pt;color:#666666;font-size:12pt;padding-bottom:4pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h5{padding-top:12pt;color:#666666;font-size:11pt;padding-bottom:4pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h6{padding-top:12pt;color:#666666;font-size:11pt;padding-bottom:4pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;font-style:italic;orphans:2;widows:2;text-align:left}
</style>
</head>
<body class="c27">
<p class="c14 c26 title" id="h.ue08p2pek5r1">
<span class="c5">
</span>
</p>
<a id="t.0ca98c45233da4884968c2ea333bc7e094b5dd3c">
</a>
<a id="t.0">
</a>
<table class="c28">
<tbody>
<tr class="c24">
<td class="c15" colspan="1" rowspan="1">
<p class="c29">
<span class="c17">If you like this article, come work with me at DoiT International, where I am a cloud architect. Write me, or
</span>
<span class="c25 c17">
<a class="c8" href="https://www.google.com/url?q=https://grnh.se/55e74b343us">&nbsp;send your resume here
</a>
</span>
<span class="c17">. Also, see
</span>
<span class="c17 c25">
<a class="c8" href="https://www.google.com/url?q=https://blog.doit-intl.com/why-i-work-at-doit-as-a-cloud-infrastructure-consultant-a87fceb74a73?source%3Dfriends_link%26sk%3De77a2a330fc3904002542404834f7a0c&amp;sa=D&amp;source=editors&amp;ust=1639920609310000&amp;usg=AOvVaw2JcJWrNW_wnFb87RbPQFOw">my blog post
</a>
</span>
<span class="c17">&nbsp;on our unusual way of working.
</span>
</p>
</td>
</tr>
</tbody>
</table>
<p class="c14 c26 title" id="h.tg4j5ms8ffaq">
<span class="c6 c22">
</span>
</p>
<p class="c13">
<span class="c3">
<a href="https://joshuafox.com/yiddish/%25D7%25A7%25D7%2595%25D7%2591%25D7%25A2%25D7%25A8%25D7%25A0%25D7%25A2%25D7%2598%25D7%25A2%25D7%25A1" style="color:inherit;text-decoration:inherit">
The Yiddish original is here</a></span><span class="c17 c6 c21">.
</span>
</p>
<p class="c1">
<span class="c21 c17 c6">
</span>
</p>
<p class="c14 title" id="h.af1dw7iqhut">
<span>Kubernetes: The simple way to run complex server applications
</span>
</p>
<h3 class="c11" id="h.ma3m8hx8el4h">
<span class="c6">Kubernetes addresses the problem of running complex server applications with many parts.
</span>
</h3>
<h3 class="c1 c23" id="h.c86dt9npyono">
<span class="c4">
</span>
</h3>
<h3 class="c11" id="h.c86dt9npyono-1">
<span class="c4">First, the parts: Over the decades, computing has moved to higher and higher levels of abstraction. From hardware computers, we moved to virtual machines. But since 2015, a new abstraction has emerged, the container: A portable, lightweight bundle of functionality--i.e., part of an application--that can run on a virtual machine.
</span>
</h3>
<p class="c1" dir="rtl">
<span class="c4">
</span>
</p>
<h3 class="c11" id="h.gmnug911ykxi">
<span class="c4">A container is not a virtual machine: it is simply a well-protected directory with the files of an application, which can be downloaded to a virtual machine and used without worrying about other files in the virtual machine.
</span>
</h3>
<h3 class="c1 c23" id="h.jaoqv5yyb7ht">
<span class="c4">
</span>
</h3>
<h3 class="c11" id="h.hpjexqk6baao">
<span class="c4">Second, the orchestration: As cloud platforms allow software systems to grow in complexity and size, managing them automatically becomes all the more important.
</span>
</h3>
<h3 class="c1 c23" id="h.fk7quacpal3z">
<span class="c4">
</span>
</h3>
<h3 class="c11" id="h.eihqodxa39nd">
<span class="c4">Kubernetes was invented for this: It orchestrates software containers. That is, it launches containers and ensures that they remain running; it defines communication between them; it adds more containers to serve an application in accordance with the load; and so on.
</span>
</h3>
<p class="c1">
<span class="c4">
</span>
</p>
<h3 class="c11" id="h.3a2w64ovjb5i">
<span class="c4">Is Kubernetes really necessary? No--software ran fine for years before Kubernetes. However, if your cloud-based server is more than moderately complicated, you&rsquo;ll find that Kubernetes makes your life easier. It is also the standard for cloud orchestration, and so will let you take advantage of the large variety of third-party software that works with it.
</span>
</h3>
<p class="c1">
<span class="c4">
</span>
</p>
<h3 class="c11" id="h.r5417w8zxit9">
<span class="c6">Kubernetes has a number of concepts that help organize the orchestration, like &ldquo;Pod,&rdquo; &ldquo;Deployment&rdquo; and &ldquo;Service.&rdquo; The details of these definitions are not important at this point. But for a short overview: A Pod is a container which is running in the cloud, sometimes with some auxiliary containers; A Deployment is a group of copies of a pod which serves an application; and a Service exposes an application for access at a certain address.
</span>
</h3>
<p class="c1" dir="rtl">
<span class="c4">
</span>
</p>
<h3 class="c11" id="h.kd3d622sgz3">
<span class="c4">Now I will lead you through a little &ldquo;Hello World&rdquo; example--according to time-honoured custom--to show the usage of Kubernetes: How you run a simple server.
</span>
</h3>
<p class="c1" dir="rtl">
<span class="c4">
</span>
</p>
<ol class="c7 lst-kix_uzlu6ke0i96j-0 start" start="1">
<li class="c11 c19 li-bullet-0">
<h3 id="h.wex73eenqczn" style="display:inline">
<span class="c4">First, create a cluster, a collection of virtual machines in which your containers will run.
</span>
</h3>
</li>
</ol>
<ul class="c7 lst-kix_prhopwzg51ya-0 start">
<li class="c2 li-bullet-0">
<h3 id="h.wex73eenqczn-2" style="display:inline">
<span class="c4">Register for Google Cloud. There is a free option.
</span>
</h3>
</li>
<li class="c2 li-bullet-0">
<h3 id="h.wex73eenqczn-3" style="display:inline">
<span class="c4">Go to Google Kubernetes Engine in the Cloud Console and click &ldquo;CREATE&rdquo; and then &ldquo;CONFIGURE&rdquo; next to &ldquo;Standard. Next: &ldquo;My first cluster&rdquo; and &ldquo;CREATE NOW&rdquo;.
</span>
</h3>
</li>
</ul>
<p class="c1 c18" dir="rtl">
<span class="c4">
</span>
</p>
<h3 class="c1 c23" id="h.c9yc2pthbyw4">
<span class="c4">
</span>
</h3>
<ol class="c7 lst-kix_uzlu6ke0i96j-0" start="2">
<li class="c11 c19 li-bullet-0">
<h3 id="h.c9yc2pthbyw4-4" style="display:inline">
<span class="c4">Second, enter the Cloud Shell, a virtual machine in the cloud dedicated to you; you can give commands as in a shell on any computer. (And in fact you can do this on your laptop.)
</span>
</h3>
</li>
</ol>
<ul class="c7 lst-kix_gj9eps2krm16-0 start">
<li class="c2 li-bullet-0">
<h3 id="h.c9yc2pthbyw4-5" style="display:inline">
<span class="c4">Click the name of the cluster.
</span>
</h3>
</li>
<li class="c2 li-bullet-0">
<h3 id="h.c9yc2pthbyw4-6" style="display:inline">
<span class="c4">Click &ldquo;CONNECT&rdquo; and &ldquo;RUN IN CLOUD SHELL&rdquo; to go to the Cloud Shell. You will see a command line like
</span>
</h3>
</li>
<li class="c2 li-bullet-0">
<h3 id="h.c9yc2pthbyw4-7" style="display:inline">
<span class="c6">&nbsp;
</span>
<span class="c0">gcloud clusters get-credentials my-first-cluster-1 --zone us-central1-c --project
</span>
<span class="c6">&nbsp;
</span>
<span class="c0 c9">my-project
</span>
</h3>
</li>
<li class="c2 li-bullet-0">
<h3 id="h.c9yc2pthbyw4-8" style="display:inline">
<span class="c4">Type Enter to &nbsp;run this command and connect to the cluster.
</span>
</h3>
</li>
<li class="c2 li-bullet-0">
<h3 id="h.m3sppqxujqcs" style="display:inline">
<span class="c4">Click &ldquo;AUTHORIZE&rdquo; if this appears.
</span>
</h3>
</li>
</ul>
<p class="c1">
<span class="c4">
</span>
</p>
<ol class="c7 lst-kix_uzlu6ke0i96j-0" start="3">
<li class="c11 c19 li-bullet-0">
<h3 id="h.foyqjegfk3l0" style="display:inline">
<span class="c4">Third, launch everything based on definitions in a yaml file:
</span>
</h3>
</li>
</ol>
<ul class="c7 lst-kix_a3bncohmjifs-0 start">
<li class="c2 li-bullet-0">
<h3 id="h.qmy5q45uwjsu" style="display:inline">
<span class="c4">You can look at this file in the address in this command and see the definitions of the Deployment and Service.
</span>
</h3>
</li>
</ul>
<h3 class="c11 c20" id="h.au0dcoxig1ny">
<span class="c0">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;kubectl apply -f https://joshuafox.com/content/sholem.yaml
</span>
</h3>
<ul class="c7 lst-kix_qghhohyfbmul-0 start">
<li class="c2 li-bullet-0">
<h3 id="h.foyqjegfk3l0-9" style="display:inline">
<span class="c4">Type that command.
</span>
</h3>
</li>
</ul>
<p class="c1 c20">
<span class="c4">
</span>
</p>
<ol class="c7 lst-kix_uzlu6ke0i96j-0" start="4">
<li class="c11 c19 li-bullet-0">
<h3 id="h.6qjv33jvshrp" style="display:inline">
<span class="c6">After about three minutes, type
</span>
<span class="c0 c12">kubectl get service,deployment
</span>
<span class="c4">.
</span>
</h3>
</li>
</ol>
<ul class="c7 lst-kix_g0gsqjenso1g-0 start">
<li class="c2 li-bullet-0">
<h3 id="h.2vbgma5w7sl2" style="display:inline">
<span class="c6">Next to the service
</span>
<span class="c0">sholem-service
</span>
<span class="c4">, you will see an address under &ldquo;External-IP&rdquo;; and next to the deployment, you will see &ldquo;1/1&rdquo; indicating that the one pod is running. If you don&rsquo;t see these, wait 3 minutes and try again.
</span>
</h3>
</li>
<li class="c2 li-bullet-0">
<h3 id="h.evgme7qyfv56" style="display:inline">
<span class="c6">Open the Internet Protocol address as
</span>
<span class="c0 c12">34.69.48.156
</span>
<span class="c4">in the example, in a browser and see a web-page from the server, and see a web page that says &ldquo;Hello, world&rdquo;.
</span>
</h3>
</li>
<li class="c2 li-bullet-0">
<h3 id="h.r055vavjo7hs" style="display:inline">
<span class="c4">We have reached our goal! We have a server running in the cloud, created from a predefined bundle of functionality, on infrastructure conveniently managed by Kuberenetes.
</span>
</h3>
</li>
</ul>
<p class="c13 c16" dir="rtl">
<span class="c4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span>
</p>
<p class="c1 c16" dir="rtl">
<span class="c4">
</span>
</p>
<p class="c13" dir="rtl">
<span>&nbsp;
</span>
<span class="c12 c30">&nbsp;
</span>
</p>
<p class="c1" dir="rtl">
<span class="c4">
</span>
</p>


<!-- Google Analytics -->

<script>
        (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
        (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
        m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
        })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
        ga('create', 'UA-24142341-1', 'auto');
        ga('send', 'pageview');

</script>

<!-- End Google Analytics -->

</body>
</html>
