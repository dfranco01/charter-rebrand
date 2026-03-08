create table if not exists customers(
    id int Primary Key not null,
    last_name varchar(255) not null,
    first_name varchar(255) not null,
    email varchar(255)not null,
    phone varchar(255) not null,
    inquiry varchar(255)
);

insert into customers
values(1, 'Lin', 'Kangle', 'kanglexlin@gmail.com', '323-449-8844', null);

insert into customers
values(2, 'Franco', 'David', 'david.d.franco28@gmail.com', '916-712-7316', null);

select * from customers;