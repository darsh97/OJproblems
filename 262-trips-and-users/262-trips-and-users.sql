with banned as (
    select *
    from users
    where banned = "YES"
),

rides_between_date as (
    select client_id, driver_id, request_at, status
    from trips
    where request_at between "2013-10-01" AND "2013-10-03"
), 

ride_data as (
    select request_at, substr(status, 1, 9) as status, ifnull(count(1), 0) as status_cnt
    from users as ut
    join rides_between_date rt
    on rt.client_id = ut.users_id and not exists (
        select 1
        from banned
        where users_id = rt.client_id
    ) and not exists (
        select 1
        from banned
        where users_id = rt.driver_id
    )
    group by request_at, substr(status, 1, 9)
    order by request_at
    
    
),

final_data as (

    select rd1.request_at as Day,  coalesce(rd1.status_cnt, 0.00) as comp_cnt,  coalesce(rd2.status_cnt, 0.00) as canc_cnt

    from (
        select *
        from ride_data
        where status = "completed"
    ) rd1
    left join (
        select *
        from ride_data
        where status = "cancelled"
    ) rd2
    on rd1.request_at = rd2.request_at and rd1.status = "completed" and rd2.status = "cancelled"


    union
    
    select rd2.request_at as Day, coalesce(rd1.status_cnt, 0.00) as comp_cnt,  coalesce(rd2.status_cnt, 0.00) as canc_cnt
    from (
        select *
        from ride_data
        where status = "completed"
    ) rd1
    right join (
        select *
        from ride_data
        where status = "cancelled"
    ) rd2
    on rd1.request_at = rd2.request_at and rd1.status = "completed" and rd2.status = "cancelled"

)

select Day, round((canc_cnt / (comp_cnt + canc_cnt)), 2) as `Cancellation Rate`
from final_data