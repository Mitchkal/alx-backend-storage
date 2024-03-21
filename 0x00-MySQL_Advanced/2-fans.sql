-- ranks country origins of bands ordered b number of non unique fans

SELECT origin AS origin, COUNT(fans) as nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
