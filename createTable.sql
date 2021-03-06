CREATE TABLE `nba_stats`.`2020_2021` (
`team_id` INT NOT NULL,
`team_name` VARCHAR(45) NOT NULL,
`gp` INT NOT NULL,
`w` INT NOT NULL,
`l` INT NOT NULL,
`w_pct` DOUBLE NOT NULL,
`min` DOUBLE NOT NULL,
`fgm` DOUBLE NOT NULL,
`fga` DOUBLE NOT NULL,
`fg_pct` DOUBLE NOT NULL,
`fg3m` DOUBLE NOT NULL,
`fg3a` DOUBLE NOT NULL,
`fg3_pct` DOUBLE NOT NULL,
`ftm` DOUBLE NOT NULL,
`fta`  DOUBLE NOT NULL,
`ft_pct` DOUBLE NOT NULL,
`oreb` DOUBLE NOT NULL,
`dreb` DOUBLE NOT NULL,
`reb` DOUBLE NOT NULL,
`ast` DOUBLE NOT NULL,
`tov` DOUBLE NOT NULL,
`stl` DOUBLE NOT NULL,
`blk` DOUBLE NOT NULL,
`blka` DOUBLE NOT NULL,
`pf` DOUBLE NOT NULL,
`pfd` DOUBLE NOT NULL,
`pts` DOUBLE NOT NULL,
`plus_minus` DOUBLE NOT NULL,
`gp_rank` INT NOT NULL,
`w_rank` INT NOT NULL,
`l_rank` INT NOT NULL,
`w_pct_rank` INT NOT NULL,
`min_rank` INT NOT NULL,
`fgm_rank` INT NOT NULL,
`fga_rank` INT NOT NULL,
`fg_pct_rank` INT NOT NULL,
`fg3m_rank` INT NOT NULL,
`fg3a_rank` INT NOT NULL,
`fg3_pct_rank` INT NOT NULL,
`ftm_rank` INT NOT NULL,
`fta_rank` INT NOT NULL,
`ft_pct_rank` INT NOT NULL,
`oreb_rank` INT NOT NULL,
`dreb_rank` INT NOT NULL,
`reb_rank` INT NOT NULL,
`ast_rank` INT NOT NULL,
`tov_rank` INT NOT NULL,
`stl_rank` INT NOT NULL,
`blk_rank` INT NOT NULL,
`blka_rank` INT NOT NULL,
`pf_rank` INT NOT NULL,
`pfd_rank` INT NOT NULL,
`pts_rank` INT NOT NULL,
`plus_minus_rank` INT NOT NULL,
`cfid` INT NOT NULL,
`cfparams` VARCHAR(45) NOT NULL,
PRIMARY KEY (team_id)
);