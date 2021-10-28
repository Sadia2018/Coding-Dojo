select countries.name, languages.percentage
from countries
left join languages on countries.id = country_id
where languages.language = 'Slovene'
order by languages.percentage desc;
select countries.name as 'country', count(cities.name) as 'num cities'
from countries
left join cities on countries.id = country_id
group by countries.name
order by count(cities.name) desc;
select cities.name, cities.population
from cities
right join countries on countries.id = country_id
where countries.name = 'Mexico' and cities.population > 500000
order by cities.population desc;
select countries.name, languages.language, languages.percentage
from countries
left join languages on countries.id = country_id
where languages.percentage > 89
order by languages.percentage desc;
select countries.name 
from countries
where surface_area < 501 and population > 100000;
select countries.name
from countries
where government_form = 'Constitutional Monarchy' and capital > 200 and life_expectancy > 75;
select countries.name as 'Country Name' , cities.name as 'Cities', cities.district, cities.population
from countries
left join cities on countries.id = country_id
where countries.name = 'Argentina' and cities.district = 'Buenos Aires' and cities.population > 500000;
select countries.region, count(countries.name)
from countries
group by countries.region
order by count(countries.name) desc;


