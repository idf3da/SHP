FROM php:7.2-apache

RUN docker-php-ext-install pdo_mysql

RUN chmod -R 555 /var/www/html

COPY . /var/www/html/
