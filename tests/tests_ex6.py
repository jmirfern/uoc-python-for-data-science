"""
Tests per a l'exercici 6: Summary i Podi.
"""
# pylint: disable=wrong-import-position

import unittest
import sys
from pathlib import Path
from unittest.mock import patch

import pandas as pd

# Afegir el directori src al path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from exercises import ex6


class TestEx6(unittest.TestCase):
    """Suite de tests per a l'exercici 6."""

    def setUp(self):
        """Configura les dades de prova abans de cada test."""
        self.sample_data = pd.DataFrame({
            'HomeTeam': ['Real Madrid', 'Barcelona', 'Real Madrid', 'Barcelona'],
            'AwayTeam': ['Barcelona', 'Real Madrid', 'Atletico', 'Atletico'],
            'FTHG': [2, 1, 3, 2],
            'FTAG': [1, 2, 0, 1],
        })

        self.total_points_data = pd.DataFrame(
            {'total_points': [100, 85, 70, 60]},
            index=['Real Madrid', 'Barcelona', 'Atletico', 'Valencia']
        )

    def test_fun_total_goals(self):
        """Test que verifica el càlcul correcte de gols totals."""
        home_goals, away_goals, total_goals = ex6.fun_total_goals(self.sample_data)

        self.assertEqual(home_goals, 8)  # 2+1+3+2
        self.assertEqual(away_goals, 4)  # 1+2+0+1
        self.assertEqual(total_goals, 12)  # 8+4
        self.assertIsInstance(home_goals, int)
        self.assertIsInstance(away_goals, int)
        self.assertIsInstance(total_goals, int)

    def test_fun_total_goals_by_team(self):
        """Test que verifica el càlcul correcte de gols per equip."""
        home_goals_by_team, away_goals_by_team, total_goals_by_team = ex6.fun_total_goals_by_team(
            self.sample_data
        )

        # Verificar tipus de retorn
        self.assertIsInstance(home_goals_by_team, pd.DataFrame)
        self.assertIsInstance(away_goals_by_team, pd.DataFrame)
        self.assertIsInstance(total_goals_by_team, pd.DataFrame)

        # Verificar columnes
        self.assertIn("home_goals", home_goals_by_team.columns)
        self.assertIn("away_goals", away_goals_by_team.columns)
        self.assertIn("total_goals", total_goals_by_team.columns)

        # Verificar que està ordenat per gols totals descendents
        total_goals_values = total_goals_by_team['total_goals'].values
        self.assertTrue(
            all(
                total_goals_values[i] >= total_goals_values[i + 1]
                for i in range(len(total_goals_values) - 1)
            )
        )

    def test_fun_summary_1996_2025_with_dataframe(self):
        """Test que verifica la creació correcta del summary a partir d'un DataFrame."""
        home_goals_by_team = pd.DataFrame(
            {'home_goals': [5, 3, 2, 1]},
            index=['Real Madrid', 'Barcelona', 'Atletico', 'Valencia']
        )
        away_goals_by_team = pd.DataFrame(
            {'away_goals': [3, 4, 2, 0]},
            index=['Real Madrid', 'Barcelona', 'Atletico', 'Valencia']
        )
        total_goals_by_team = pd.DataFrame(
            {'total_goals': [8, 7, 4, 1]},
            index=['Real Madrid', 'Barcelona', 'Atletico', 'Valencia']
        )

        summary = ex6.fun_summary_1996_2025(
            self.total_points_data,
            home_goals_by_team,
            away_goals_by_team,
            total_goals_by_team
        )

        # Verificar estructura
        self.assertIsInstance(summary, pd.DataFrame)
        self.assertIn("total_points", summary.columns)
        self.assertIn("home_goals", summary.columns)
        self.assertIn("away_goals", summary.columns)
        self.assertIn("total_goals", summary.columns)

        # Verificar que està ordenat per total_points descendents
        points_values = summary['total_points'].values
        self.assertTrue(
            all(
                points_values[i] >= points_values[i + 1]
                for i in range(len(points_values) - 1)
            )
        )

    def test_fun_summary_1996_2025_with_series(self):
        """Test que verifica la creació correcta del summary a partir d'una Series."""
        total_points_series = pd.Series(
            [100, 85, 70, 60],
            index=['Real Madrid', 'Barcelona', 'Atletico', 'Valencia']
        )

        home_goals_by_team = pd.DataFrame(
            {'home_goals': [5, 3, 2, 1]},
            index=['Real Madrid', 'Barcelona', 'Atletico', 'Valencia']
        )
        away_goals_by_team = pd.DataFrame(
            {'away_goals': [3, 4, 2, 0]},
            index=['Real Madrid', 'Barcelona', 'Atletico', 'Valencia']
        )
        total_goals_by_team = pd.DataFrame(
            {'total_goals': [8, 7, 4, 1]},
            index=['Real Madrid', 'Barcelona', 'Atletico', 'Valencia']
        )

        summary = ex6.fun_summary_1996_2025(
            total_points_series,
            home_goals_by_team,
            away_goals_by_team,
            total_goals_by_team
        )

        # Verificar que funciona amb Series
        self.assertIsInstance(summary, pd.DataFrame)
        self.assertEqual(len(summary), 4)

    def test_summary_data_types(self):
        """Test que verifica que els tipus de dades del summary són correctes."""
        home_goals_by_team = pd.DataFrame(
            {'home_goals': [5, 3]},
            index=['Real Madrid', 'Barcelona']
        )
        away_goals_by_team = pd.DataFrame(
            {'away_goals': [3, 4]},
            index=['Real Madrid', 'Barcelona']
        )
        total_goals_by_team = pd.DataFrame(
            {'total_goals': [8, 7]},
            index=['Real Madrid', 'Barcelona']
        )

        summary = ex6.fun_summary_1996_2025(
            self.total_points_data.head(2),
            home_goals_by_team,
            away_goals_by_team,
            total_goals_by_team
        )

        # Verificar tipus de dades
        self.assertEqual(summary["total_points"].dtype, "int64")
        self.assertEqual(summary["home_goals"].dtype, "int64")
        self.assertEqual(summary["away_goals"].dtype, "int64")
        self.assertEqual(summary["total_goals"].dtype, "int64")

    @patch('matplotlib.pyplot.savefig')
    @patch('matplotlib.pyplot.close')
    def test_podium_creates_plot(self, mock_close, mock_savefig):
        """Test que verifica que podium genera el gràfic correctament."""
        podium_data = pd.DataFrame(
            {'total_points': [100, 85, 70, 60]},
            index=['Real Madrid', 'Barcelona', 'Atletico', 'Valencia']
        )

        # No ha de llançar excepcions
        ex6.podium(podium_data)

        # Verificar que s'ha desat la imatge
        mock_savefig.assert_called_once()
        mock_close.assert_called_once()


class TestEx6Integration(unittest.TestCase):
    """Tests d'integració per a l'exercici 6."""

    def setUp(self):
        """Configura les dades per als tests d'integració."""
        self.larger_data = pd.DataFrame({
            'HomeTeam': ['Real Madrid'] * 5 + ['Barcelona'] * 5,
            'AwayTeam': ['Barcelona', 'Atletico'] * 5,
            'FTHG': [2, 1, 3, 2, 1, 1, 2, 2, 3, 1],
            'FTAG': [1, 2, 0, 1, 2, 2, 1, 0, 1, 2],
        })

    def test_workflow_consistency(self):
        """Test que verifica la consistència del flux complet."""
        # Calcular gols
        home_goals, away_goals, _total_goals = ex6.fun_total_goals(self.larger_data)

        # Calcular gols per equip
        home_goals_by_team, away_goals_by_team, total_goals_by_team = ex6.fun_total_goals_by_team(
            self.larger_data
        )

        # Crear punts (simulat)
        total_points = pd.Series(
            [100, 85],
            index=['Real Madrid', 'Barcelona']
        ).to_frame("total_points")

        # Crear summary
        summary = ex6.fun_summary_1996_2025(
            total_points,
            home_goals_by_team,
            away_goals_by_team,
            total_goals_by_team
        )

        # Verificacions
        self.assertEqual(len(summary), 3)
        self.assertGreater(home_goals + away_goals, 0)


if __name__ == '__main__':
    unittest.main()
