# Laravel Docs for Wox
A wox plugin for searching through Laravel's documentation.

![Screenshot](https://raw.githubusercontent.com/matical/wox-laravel-docs/master/search.png)

## Requirements
* Python >3.6 in path
* algoliasearch-client-python (`pip install algoliasearch`)
    - This plugin ~~jacks~~ queries the same Algolia API *available* on the laravel.com/docs site.

## Install
For now, just clone this repo into your plugin directory.

## Usage
```
ld <query>
```

By default, the `master` branch will be used for queries. If you wish to search a specific branch, use `ld <branch>:<query>`.

```
ld 5.0:remote
```