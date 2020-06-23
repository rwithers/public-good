drop table if exists call cascade;
drop index if exists call_hash_code_idx;

create table call (
    call_id             serial8, 
    hash_code           varchar, 
    date                timestamp, 
    precinct            varchar, 
    address             varchar, 
    status_code         varchar,
    location_lat        decimal,
    location_lon        decimal,
    extended_address    json,
    primary key (call_id)
);

alter table call add column geom geometry(point,4326);

create index call_hash_code_idx on call (hash_code);

