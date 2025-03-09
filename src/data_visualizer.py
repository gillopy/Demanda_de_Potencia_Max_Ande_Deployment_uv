import seaborn as sns
import matplotlib.pyplot as plt

class DataVisualizer:
    def __init__(self, analyzer):
        self.analyzer = analyzer
        self.orden_meses = [
            'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
            'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
        ]
        self.g = None

    def plot(self):
        """Genera la visualización completa"""
        sns.set_theme(style="white")
        self._create_base_plot()
        self._customize_subplots()
        self._apply_final_touches()
        plt.show()
    
    def _create_base_plot(self):
        """Crea la estructura base del gráfico"""
        self.g = sns.relplot(
            data=self.analyzer.df_melted,
            x="Mes", y="KWh", col="Año", hue="Año",
            kind="line", palette="crest", linewidth=4, zorder=5,
            col_wrap=3, height=5, aspect=2, legend=False
        )
    
    def _customize_subplots(self):
        """Personaliza cada subgráfico individual"""
        for año, ax in self.g.axes_dict.items():
            self._add_title(ax, año)
            self._add_background_lines(ax)
            self._format_axes(ax)
            self._add_vertical_lines(ax)
            self._add_annual_mean(ax, año)
            self._add_monthly_ticks(ax)
            self._add_plot_border(ax)
    
    def _add_title(self, ax, año):
        """Añade título al subgráfico"""
        ax.text(
            0.9, 0.9, str(año),
            transform=ax.transAxes,
            fontweight="bold",
            bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.1')
        )
    
    def _add_background_lines(self, ax):
        """Añade líneas de fondo para contexto"""
        sns.lineplot(
            data=self.analyzer.df_melted,
            x="Mes", y="KWh", units="Año",
            estimator=None, color=".7", linewidth=1, ax=ax
        )
    
    def _format_axes(self, ax):
        """Formatea ejes y etiquetas"""
        ax.tick_params(axis='x', rotation=90)
        ax.set_xticks(range(len(self.orden_meses)))
        ax.set_xticklabels(self.orden_meses)
        ax.set_xlim(-0.5, len(self.orden_meses) - 0.5)
    
    def _add_vertical_lines(self, ax):
        """Añade líneas verticales de referencia"""
        ax.axvline(x=2, color='red', linestyle='--', linewidth=0.8, label='Marzo')
        ax.axvline(x=8, color='red', linestyle='--', linewidth=0.8, label='Septiembre')
    
    def _add_annual_mean(self, ax, año):
        """Añade línea de promedio anual"""
        promedio = self.analyzer.annual_stats[año]
        ax.plot(
            self.orden_meses,
            [promedio] * len(self.orden_meses),
            color='green', linestyle='--', linewidth=1,
            label=f'Promedio Anual MW: {promedio:.0f}'
        )
        ax.legend()
    
    def _add_monthly_ticks(self, ax):
        """Añade marcas mensuales"""
        for idx in range(len(self.orden_meses)):
            ax.axvline(x=idx, color='black', linestyle='--', alpha=0.3, linewidth=0.2)
    
    def _add_plot_border(self, ax):
        """Añade borde al subgráfico"""
        ax.patch.set_edgecolor('black')
        ax.patch.set_linewidth(1)
    
    def _apply_final_touches(self):
        """Aplica ajustes finales al gráfico"""
        self.g.set_titles("")
        self.g.set_axis_labels("", "MW")
        plt.tight_layout()
    
    def save_plot(self, filename="grafico_demandaactual.png", dpi=200):
        """Guarda el gráfico en archivo"""
        if self.g is None:
            self.plot()  # Genera el gráfico si no existe
        self.g.savefig(filename, dpi=dpi, bbox_inches="tight")