CREATE TABLE cars (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    year INT,
    selling_price DECIMAL(10,2),
    km_driven INT,
    fuel VARCHAR(50),
    seller_type VARCHAR(50),
    transmission VARCHAR(50),
    owner VARCHAR(50)
);
