from simulate_card import simulate_runs
import pandas as pd
from plotnine import *


def main():
    ###Simulate the necessary card runs
    simulate_array = simulate_runs()

    ###Convert to pandas for plot9
    simulate_df = pd.DataFrame(simulate_array, columns=["10", "15", "20", "25","30","35"])
    simulate_df["Runs"] = range(1000)
    simulate_df_melted = pd.melt(simulate_df, id_vars = ["Runs"])

    ###Create another data.frame that is the average
    column_means = pd.DataFrame(simulate_df.iloc[:, :6].mean(axis=0)).reset_index()
    column_means.columns = ["variable", "value"]


    ###making the plot
    p = (
        ggplot(simulate_df_melted) +
        geom_jitter(
            aes(x="variable", y="value", group="variable"),
            width=0.1,
            alpha = 0.35
        ) + 
        geom_line(
            aes(x="variable", y="value", group=1),
            data=column_means,
            color="black" ) +
        geom_point(
            aes(x="variable", y="value", group=1),
            data=column_means,
            color="red" )  + 
        xlab("Total number of Cards") + 
        ylab("Total number of turns") + 
    theme_bw()
)


    
    p.save("simulation_plot.png", width=8, height=6, dpi=300)


if __name__ == "__main__":
    main()