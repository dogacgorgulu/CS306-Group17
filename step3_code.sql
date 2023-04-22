-- Views

-- A view of top 20 countries with most total deaths
CREATE VIEW top_20_deaths AS
SELECT iso_code, SUM(from_droughts + from_earthquakes + from_volcanoes + from_floods + from_storms + from_landslides + from_wildfired + from_extreme_temperatures) as total_deaths
FROM deaths
GROUP BY iso_code
ORDER BY total_deaths DESC
LIMIT 20;

-- A view of top 20 countries with most total injuries
CREATE VIEW top_20_injuries AS
SELECT iso_code, SUM(from_droughts + from_earthquakes + from_volcanoes + from_floods + from_storms + from_landslides + from_wildfired + from_extreme_temperatures) as total_injuries
FROM injuries
GROUP BY iso_code
ORDER BY total_injuries DESC
LIMIT 20;

-- A view of top 20 countries with most people in the year 2020
CREATE VIEW top_20_populated_countries AS
Select iso_code, MAX(population) AS population, the_year
From population
WHERE the_year = 2020
Group By iso_code
ORDER BY population DESC
LIMIT 20;

-- A view of countries that suffered more than average economic damages
CREATE VIEW heavily_economically_damaged AS
SELECT iso_code, SUM(total_insured_damages + total_reconstruction_costs + total_economic_damages) AS all_damages
FROM economic_damage
GROUP BY iso_code
HAVING all_damages > (SELECT AVG(total_insured_damages + total_reconstruction_costs + total_economic_damages) FROM economic_damage);

-- A view of top 20 countries with most affected people
CREATE VIEW top_20_affected AS
SELECT iso_code, SUM(from_droughts + from_earthquakes + from_volcanoes + from_floods + from_storms + from_landslides + from_wildfired + from_extreme_temperatures) as total_affected
FROM affected
GROUP BY iso_code
ORDER BY total_affected DESC
LIMIT 20;

-- Aggragate operators

-- Using SUM, get the total economic impact
SELECT iso_code, the_year, SUM(total_insured_damages + total_reconstruction_costs + total_economic_damages) AS total_costs 
FROM economic_damage
GROUP BY iso_code, the_year;

-- Using MAX, get the country with the highest number of deaths
SELECT iso_code, total_deaths
FROM top_20_deaths 
GROUP BY iso_code
HAVING total_deaths = (SELECT MAX(total_deaths) FROM top_20_deaths);

-- Using MIN, get the minimum number of injuries from earthquakes that is bigger than 100 by year
SELECT the_year, MIN(from_earthquakes)
FROM injuries 
WHERE from_earthquakes > 100
GROUP BY the_year
ORDER BY the_year DESC;

-- Using COUNT, get the number of countries
SELECT COUNT(iso_code) AS NumberOfCountries FROM countries;

-- Using AVG, get the countries with a higher than average injuries from earthquakes by year
SELECT iso_code, the_year, from_earthquakes
FROM injuries 
GROUP BY iso_code, the_year
HAVING from_earthquakes > (SELECT AVG(from_earthquakes) FROM injuries);

-- Procedure to get the number of people injured from earthquakes by year
DELIMITER //
CREATE PROCEDURE get_earthquake_inj (given_year INT)
BEGIN
    SELECT iso_code, the_year, from_earthquakes FROM injuries WHERE from_earthquakes > 0 AND the_year = given_year;
END //
DELIMITER ;

-- These two return different results
CALL get_earthquake_inj(2000);
CALL get_earthquake_inj(2010);

-- Showing in and exists returns the same when used correctly
-- We get countries that have an higher than average economic damage
SELECT countries.country_name FROM countries
WHERE countries.iso_code IN (SELECT economic_damage.iso_code FROM economic_damage
WHERE economic_damage.total_economic_damages > (SELECT AVG(total_economic_damages) FROM economic_damage));

SELECT countries.country_name
FROM countries
WHERE EXISTS (SELECT *
FROM economic_damage
WHERE economic_damage.total_economic_damages > (SELECT AVG(total_economic_damages) FROM economic_damage) AND countries.iso_code=economic_damage.iso_code);

-- Joins

-- Countries in top 20 deaths view displayed with their populations
SELECT top_20_deaths.iso_code, population.population, top_20_deaths.total_deaths
FROM top_20_deaths
JOIN population
ON top_20_deaths.iso_code = population.iso_code
AND population.the_year = 2020
ORDER BY top_20_deaths.total_deaths DESC;

-- Another join showing more information
SELECT 
    p.iso_code, 
    p.population AS population_2020, 
    COALESCE(SUM(d.total_deaths), 0) AS total_deaths, 
    COALESCE(SUM(i.total_injuries), 0) AS total_injuries, 
    COALESCE(SUM(a.total_affected), 0) AS total_affected
FROM 
    population p 
    LEFT JOIN top_20_deaths d ON p.iso_code = d.iso_code 
    LEFT JOIN top_20_injuries i ON p.iso_code = i.iso_code 
    LEFT JOIN top_20_affected a ON p.iso_code = a.iso_code 
WHERE 
    p.the_year = 2020
GROUP BY 
    p.iso_code, 
    p.population
ORDER BY 
    (COALESCE(SUM(d.total_deaths), 0) + COALESCE(SUM(i.total_injuries), 0) + COALESCE(SUM(a.total_affected), 0)) DESC
LIMIT 
    20;
    
-- Top 20 countries with total deaths and their total injuries if they appear on the top 20 injuries view
SELECT top_20_deaths.iso_code, top_20_deaths.total_deaths, top_20_injuries.total_injuries
FROM top_20_deaths LEFT JOIN top_20_injuries ON top_20_deaths.iso_code = top_20_injuries.iso_code;

-- Same thing, but with deaths instead of injuries and vice versa
SELECT top_20_injuries.iso_code, top_20_injuries.total_injuries, top_20_deaths.total_deaths
FROM top_20_injuries LEFT JOIN top_20_deaths ON top_20_injuries.iso_code = top_20_deaths.iso_code;

-- Countries that show up on both these views, notice that these are the only countries without null values in both tables
SELECT top_20_injuries.iso_code FROM top_20_injuries
INNER JOIN top_20_deaths ON top_20_injuries.iso_code = top_20_deaths.iso_code;