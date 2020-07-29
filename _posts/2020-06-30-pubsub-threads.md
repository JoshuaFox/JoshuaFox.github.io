---
layout: post
title: Too Many Threads in Cloud Pub/Sub
subtitle: How to slim down the Publisher to a manageable amount of threads.
bigimg:

tags: [gcp, pubsub, java, threads, googlecloud ]
---
On first use, the Google PubSub Java client creates 60 threads that stay live permanently.

<!--end.excerpt-->

Maybe that is not a problem for you, but if your application is resource-constrained and low-traffic, you don't want so many threads waiting for massive outgoing traffic that will never happen.

[More on how to solve this at  my article](https://blog.doit-intl.com/too-many-threads-in-cloud-pub-sub-fdf98c9cdb71?source=friends_link&sk=56dbff74e61ef1e1fb3e3e67f7d5c634).
