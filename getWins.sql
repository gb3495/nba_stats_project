SELECT 2015_2016.w, 2016_2017.w, 2017_2018.w, teams.team_id, teams.team_name
FROM teams
INNER JOIN 2015_2016 ON teams.team_id=2015_2016.team_id
INNER JOIN 2016_2017 ON teams.team_id=2016_2017.team_id
INNER JOIN 2017_2018 ON teams.team_id=2017_2018.team_id;