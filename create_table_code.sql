Create Table countries(
    iso_code VARCHAR(5) NOT NULL,
    country_name VARCHAR(45),
    PRIMARY KEY (iso_code)
);

Create Table population(
    iso_code VARCHAR(5) NOT NULL,
    population INT,
    the_year INT NOT NULL,
    PRIMARY KEY (iso_code,the_year),
    Foreign KEY (iso_code) REFERENCES countries(iso_code) ON DELETE CASCADE
);

Create Table economic_damage(
    iso_code VARCHAR(5) NOT NULL,
    the_year INT NOT NULL,
    total_reconstruction_costs INT,
    total_insured_damages INT,
    total_economic_damages INT,
    PRIMARY KEY (iso_code,the_year),
    Foreign KEY (iso_code) REFERENCES countries(iso_code) ON DELETE CASCADE
);

Create Table deaths(
    iso_code VARCHAR(5) NOT NULL,
    the_year INT NOT NULL,
    from_droughts INT DEFAULT NULL,
    from_earthquakes INT DEFAULT NULL,
    from_volcanoes INT DEFAULT NULL,
    from_floods INT DEFAULT NULL,
    from_storms INT DEFAULT NULL,
    from_landslides INT DEFAULT NULL,
    from_wildfired INT DEFAULT NULL,
    from_extreme_temperatures INT DEFAULT NULL,
    PRIMARY KEY (iso_code,the_year),
    Foreign KEY (iso_code) REFERENCES countries(iso_code) ON DELETE CASCADE
);

Create Table injuries(
    iso_code VARCHAR(5) NOT NULL,
    the_year INT NOT NULL,
    from_droughts INT DEFAULT NULL,
    from_earthquakes INT DEFAULT NULL,
    from_volcanoes INT DEFAULT NULL,
    from_floods INT DEFAULT NULL,
    from_storms INT DEFAULT NULL,
    from_landslides INT DEFAULT NULL,
    from_wildfired INT DEFAULT NULL,
    from_extreme_temperatures INT DEFAULT NULL,
    PRIMARY KEY (iso_code,the_year),
    Foreign KEY (iso_code) REFERENCES countries(iso_code) ON DELETE CASCADE
); 

Create Table affected(
    iso_code VARCHAR(5) NOT NULL,
    the_year INT NOT NULL,
    from_droughts INT DEFAULT NULL,
    from_earthquakes INT DEFAULT NULL,
    from_volcanoes INT DEFAULT NULL,
    from_floods INT DEFAULT NULL,
    from_storms INT DEFAULT NULL,
    from_landslides INT DEFAULT NULL,
    from_wildfired INT DEFAULT NULL,
    from_extreme_temperatures INT DEFAULT NULL,
    PRIMARY KEY (iso_code,the_year),
    Foreign KEY (iso_code) REFERENCES countries(iso_code) ON DELETE CASCADE
);