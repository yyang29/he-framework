library(dplyr)
library(ggplot2)
library(repr)
library(stringr)

# Change plot size
options(repr.plot.width=20, repr.plot.height=12)

file_path <- "/home/yang/projects/he-framework/results.csv"

# Load the data
data <- read.csv(file_path)

data$NumAlu <- factor(data$NumAlu, levels = c("16", "32", "64", "128", "256", "512"))

data$Latency <- data$Latency / 1000

head(data, 5)

plot_data <- data %>% filter(BW == 460)

# p1 <- ggplot(plot_data, aes(x = NumAlu, y = Latency, group = Name)) +
#   geom_line(aes(color = Name)) + 
#   geom_point(aes(shape = Name, color = Name)) +
#   facet_wrap(~ Op, scales = "free_y", nrow = 1) +
#   labs(title = "", x = "NumAlu", y = "Latency [ms]") +
#   # theme_minimal() +
#   theme(
#     plot.title = element_text(hjust = 0.5, size = 20, face = "bold"),
#     axis.title.x = element_text(size = 12, face = "bold"),
#     axis.title.y = element_text(size = 12, face = "bold"),
#     axis.text.x = element_text(size = 12),
#     axis.text.y = element_text(size = 12),
#     legend.title = element_text(size = 12, face = "bold"),
#     legend.text = element_text(size = 12),
#     strip.text = element_text(size = 12)
#   ) +
#   theme(legend.position="top", legend.box.margin = margin(t = 0, b = -10, unit = "pt"))
#   # theme(strip.background = element_rect(colour = "black", fill = "white", size = 1),
#   #       panel.border = element_rect(colour = "black", fill = "NA", size = 1))

# ggsave("./figure1.png", plot=p1, width=9, height=2.5, dpi=300)

plot_data <- data %>% filter(Op != "Rotate")
plot_data <- plot_data %>% filter(NumAlu != "16")

p1 <- ggplot(plot_data, aes(x = NumAlu, y = Latency, fill = factor(BW))) +
  geom_bar(color="black", stat = "identity", position="dodge", linewidth=0.3) +
  facet_wrap(~ interaction(Op, Name, sep = " | "), scales = "free_y", nrow = 3) +
  labs(title = element_blank(), x = "NumAlu", y = "Latency [ms]") +
  # theme_minimal() +
  theme(
    plot.title = element_text(hjust = 0.5, size = 20, face = "bold"),
    axis.title.x = element_text(size = 16, face = "bold"),
    axis.title.y = element_text(size = 16, face = "bold"),
    axis.text.x = element_text(size = 14),
    axis.text.y = element_text(size = 14),
    legend.title = element_text(size = 16, face = "bold"),
    legend.text = element_text(size = 16),
    strip.text = element_text(size = 14)
  ) +
  theme(legend.position="top", legend.box.margin = margin(t = -10, b = -10, unit = "pt")) +
  guides(fill=guide_legend(title="BW [GB/s]"))
  # theme(strip.background = element_rect(colour = "black", fill = "white", size = 1),
  #       panel.border = element_rect(colour = "black", fill = "NA", size = 1))

ggsave("./dse_eval.png", plot=p1, width=8.5, height=5, dpi=300)