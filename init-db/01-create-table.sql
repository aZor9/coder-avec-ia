-- Création de la table count_table
CREATE TABLE IF NOT EXISTS count_table (
    id SERIAL PRIMARY KEY,
    count_number INTEGER NOT NULL DEFAULT 0
);

-- Insertion d'une ligne par défaut avec count_number = 0
INSERT INTO count_table (count_number) VALUES (0)
ON CONFLICT DO NOTHING;