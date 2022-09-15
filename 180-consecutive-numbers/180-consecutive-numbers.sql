select distinct T.first as `ConsecutiveNums`

from (
    select 
        l1.id,
        l1.num as first,
        lead(l1.num) over(order by l1.id) as second,
        lead(l2.num) over(order by l2.id) as third

    from logs l1, logs l2
    where (l1.id +1 = l2.id)
    
) T
where T.first = T.second and T.second = T.third