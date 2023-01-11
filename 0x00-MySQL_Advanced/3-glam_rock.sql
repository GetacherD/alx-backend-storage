-- Script that list all bands with Glam rock as their main style
-- ranked by their longevity
SELECT band_name,  IFNULL(split, NOW())-formed AS
lifespan FROM metal_bands
WHERE style LIKE "%Glam rock%" ORDER BY TO_DAYS(IFNULL(split, NOW())) - TO_DAYS(formed) DESC;
