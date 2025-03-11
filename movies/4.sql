SELECT COUNT(*) FROM movies WHERE id = (SELECT move_id FROM ratings WHERE rating = 10)
