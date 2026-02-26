namespace Lab2
{
    partial class Form1
    {
        /// <summary>
        /// Обязательная переменная конструктора.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Освободить все используемые ресурсы.
        /// </summary>
        /// <param name="disposing">истинно, если управляемый ресурс должен быть удален; иначе ложно.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Код, автоматически созданный конструктором форм Windows

        /// <summary>
        /// Требуемый метод для поддержки конструктора — не изменяйте 
        /// содержимое этого метода с помощью редактора кода.
        /// </summary>
        private void InitializeComponent()
        {
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea1 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            System.Windows.Forms.DataVisualization.Charting.Legend legend1 = new System.Windows.Forms.DataVisualization.Charting.Legend();
            System.Windows.Forms.DataVisualization.Charting.Series series1 = new System.Windows.Forms.DataVisualization.Charting.Series();
            this.panel1 = new System.Windows.Forms.Panel();
            this.inputStep = new System.Windows.Forms.NumericUpDown();
            this.btnClear = new System.Windows.Forms.Button();
            this.label10 = new System.Windows.Forms.Label();
            this.inputLambda = new System.Windows.Forms.NumericUpDown();
            this.label9 = new System.Windows.Forms.Label();
            this.inputHeat = new System.Windows.Forms.NumericUpDown();
            this.label8 = new System.Windows.Forms.Label();
            this.inputPlot = new System.Windows.Forms.NumericUpDown();
            this.label7 = new System.Windows.Forms.Label();
            this.btnStart = new System.Windows.Forms.Button();
            this.inputTime = new System.Windows.Forms.NumericUpDown();
            this.label6 = new System.Windows.Forms.Label();
            this.inputDelta = new System.Windows.Forms.NumericUpDown();
            this.label5 = new System.Windows.Forms.Label();
            this.inputStartTemp = new System.Windows.Forms.NumericUpDown();
            this.label4 = new System.Windows.Forms.Label();
            this.inputRight = new System.Windows.Forms.NumericUpDown();
            this.label3 = new System.Windows.Forms.Label();
            this.inputLeft = new System.Windows.Forms.NumericUpDown();
            this.label2 = new System.Windows.Forms.Label();
            this.inputWidth = new System.Windows.Forms.NumericUpDown();
            this.label1 = new System.Windows.Forms.Label();
            this.chart1 = new System.Windows.Forms.DataVisualization.Charting.Chart();
            this.dataGridResults = new System.Windows.Forms.DataGridView();
            this.dtValue = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.h = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.Tmiddle = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.endTime = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.panel1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.inputStep)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputLambda)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputHeat)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputPlot)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputTime)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputDelta)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputStartTemp)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputRight)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputLeft)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputWidth)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.chart1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridResults)).BeginInit();
            this.SuspendLayout();
            // 
            // panel1
            // 
            this.panel1.BackColor = System.Drawing.SystemColors.HotTrack;
            this.panel1.Controls.Add(this.inputStep);
            this.panel1.Controls.Add(this.btnClear);
            this.panel1.Controls.Add(this.label10);
            this.panel1.Controls.Add(this.inputLambda);
            this.panel1.Controls.Add(this.label9);
            this.panel1.Controls.Add(this.inputHeat);
            this.panel1.Controls.Add(this.label8);
            this.panel1.Controls.Add(this.inputPlot);
            this.panel1.Controls.Add(this.label7);
            this.panel1.Controls.Add(this.btnStart);
            this.panel1.Controls.Add(this.inputTime);
            this.panel1.Controls.Add(this.label6);
            this.panel1.Controls.Add(this.inputDelta);
            this.panel1.Controls.Add(this.label5);
            this.panel1.Controls.Add(this.inputStartTemp);
            this.panel1.Controls.Add(this.label4);
            this.panel1.Controls.Add(this.inputRight);
            this.panel1.Controls.Add(this.label3);
            this.panel1.Controls.Add(this.inputLeft);
            this.panel1.Controls.Add(this.label2);
            this.panel1.Controls.Add(this.inputWidth);
            this.panel1.Controls.Add(this.label1);
            this.panel1.Location = new System.Drawing.Point(784, 1);
            this.panel1.Margin = new System.Windows.Forms.Padding(4);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(282, 617);
            this.panel1.TabIndex = 0;
            // 
            // inputStep
            // 
            this.inputStep.DecimalPlaces = 4;
            this.inputStep.Increment = new decimal(new int[] {
            1,
            0,
            0,
            262144});
            this.inputStep.Location = new System.Drawing.Point(128, 260);
            this.inputStep.Margin = new System.Windows.Forms.Padding(4);
            this.inputStep.Maximum = new decimal(new int[] {
            1,
            0,
            0,
            0});
            this.inputStep.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            262144});
            this.inputStep.Name = "inputStep";
            this.inputStep.Size = new System.Drawing.Size(87, 22);
            this.inputStep.TabIndex = 20;
            this.inputStep.Value = new decimal(new int[] {
            1,
            0,
            0,
            65536});
            // 
            // btnClear
            // 
            this.btnClear.BackColor = System.Drawing.SystemColors.Info;
            this.btnClear.Location = new System.Drawing.Point(18, 565);
            this.btnClear.Margin = new System.Windows.Forms.Padding(4);
            this.btnClear.Name = "btnClear";
            this.btnClear.Size = new System.Drawing.Size(217, 43);
            this.btnClear.TabIndex = 13;
            this.btnClear.Text = "Очистить графики";
            this.btnClear.UseVisualStyleBackColor = false;
            this.btnClear.Click += new System.EventHandler(this.btnClear_Click);
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.Location = new System.Drawing.Point(124, 240);
            this.label10.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(95, 16);
            this.label10.TabIndex = 19;
            this.label10.Text = "Шаг по прост.";
            // 
            // inputLambda
            // 
            this.inputLambda.Location = new System.Drawing.Point(19, 463);
            this.inputLambda.Margin = new System.Windows.Forms.Padding(4);
            this.inputLambda.Name = "inputLambda";
            this.inputLambda.Size = new System.Drawing.Size(160, 22);
            this.inputLambda.TabIndex = 18;
            this.inputLambda.Value = new decimal(new int[] {
            46,
            0,
            0,
            0});
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Location = new System.Drawing.Point(15, 443);
            this.label9.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(208, 16);
            this.label9.TabIndex = 17;
            this.label9.Text = "Коэф. теплопроводности, Вт/м";
            // 
            // inputHeat
            // 
            this.inputHeat.Location = new System.Drawing.Point(19, 414);
            this.inputHeat.Margin = new System.Windows.Forms.Padding(4);
            this.inputHeat.Maximum = new decimal(new int[] {
            10000,
            0,
            0,
            0});
            this.inputHeat.Name = "inputHeat";
            this.inputHeat.Size = new System.Drawing.Size(160, 22);
            this.inputHeat.TabIndex = 16;
            this.inputHeat.Value = new decimal(new int[] {
            460,
            0,
            0,
            0});
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(15, 394);
            this.label8.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(206, 16);
            this.label8.TabIndex = 15;
            this.label8.Text = "Удельная теплоемкость, Дж/кг";
            // 
            // inputPlot
            // 
            this.inputPlot.Location = new System.Drawing.Point(19, 361);
            this.inputPlot.Margin = new System.Windows.Forms.Padding(4);
            this.inputPlot.Maximum = new decimal(new int[] {
            10000,
            0,
            0,
            0});
            this.inputPlot.Name = "inputPlot";
            this.inputPlot.Size = new System.Drawing.Size(160, 22);
            this.inputPlot.TabIndex = 14;
            this.inputPlot.Value = new decimal(new int[] {
            7800,
            0,
            0,
            0});
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(15, 341);
            this.label7.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(157, 16);
            this.label7.TabIndex = 13;
            this.label7.Text = "Плотность тела, кг/м^3";
            // 
            // btnStart
            // 
            this.btnStart.BackColor = System.Drawing.SystemColors.Info;
            this.btnStart.Location = new System.Drawing.Point(17, 514);
            this.btnStart.Margin = new System.Windows.Forms.Padding(4);
            this.btnStart.Name = "btnStart";
            this.btnStart.Size = new System.Drawing.Size(218, 43);
            this.btnStart.TabIndex = 12;
            this.btnStart.Text = "Запуск";
            this.btnStart.UseVisualStyleBackColor = false;
            this.btnStart.Click += new System.EventHandler(this.btnStart_Click);
            // 
            // inputTime
            // 
            this.inputTime.Location = new System.Drawing.Point(19, 311);
            this.inputTime.Margin = new System.Windows.Forms.Padding(4);
            this.inputTime.Name = "inputTime";
            this.inputTime.Size = new System.Drawing.Size(160, 22);
            this.inputTime.TabIndex = 11;
            this.inputTime.Value = new decimal(new int[] {
            2,
            0,
            0,
            0});
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(15, 292);
            this.label6.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(61, 16);
            this.label6.TabIndex = 10;
            this.label6.Text = "Время, c";
            // 
            // inputDelta
            // 
            this.inputDelta.DecimalPlaces = 4;
            this.inputDelta.Increment = new decimal(new int[] {
            1,
            0,
            0,
            262144});
            this.inputDelta.Location = new System.Drawing.Point(17, 260);
            this.inputDelta.Margin = new System.Windows.Forms.Padding(4);
            this.inputDelta.Maximum = new decimal(new int[] {
            1,
            0,
            0,
            0});
            this.inputDelta.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            262144});
            this.inputDelta.Name = "inputDelta";
            this.inputDelta.Size = new System.Drawing.Size(87, 22);
            this.inputDelta.TabIndex = 9;
            this.inputDelta.Value = new decimal(new int[] {
            1,
            0,
            0,
            65536});
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(15, 240);
            this.label5.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(90, 16);
            this.label5.TabIndex = 8;
            this.label5.Text = "Шаг по врем.";
            // 
            // inputStartTemp
            // 
            this.inputStartTemp.Location = new System.Drawing.Point(19, 208);
            this.inputStartTemp.Margin = new System.Windows.Forms.Padding(4);
            this.inputStartTemp.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.inputStartTemp.Minimum = new decimal(new int[] {
            1000,
            0,
            0,
            -2147483648});
            this.inputStartTemp.Name = "inputStartTemp";
            this.inputStartTemp.Size = new System.Drawing.Size(160, 22);
            this.inputStartTemp.TabIndex = 7;
            this.inputStartTemp.Value = new decimal(new int[] {
            27,
            0,
            0,
            0});
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(15, 188);
            this.label4.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(191, 16);
            this.label4.TabIndex = 6;
            this.label4.Text = "Начальная температура, °C:";
            // 
            // inputRight
            // 
            this.inputRight.Location = new System.Drawing.Point(19, 151);
            this.inputRight.Margin = new System.Windows.Forms.Padding(4);
            this.inputRight.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.inputRight.Minimum = new decimal(new int[] {
            1000,
            0,
            0,
            -2147483648});
            this.inputRight.Name = "inputRight";
            this.inputRight.Size = new System.Drawing.Size(160, 22);
            this.inputRight.TabIndex = 5;
            this.inputRight.Value = new decimal(new int[] {
            27,
            0,
            0,
            0});
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(15, 132);
            this.label3.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(168, 16);
            this.label3.TabIndex = 4;
            this.label3.Text = "Температура справа, °C:";
            // 
            // inputLeft
            // 
            this.inputLeft.Location = new System.Drawing.Point(19, 92);
            this.inputLeft.Margin = new System.Windows.Forms.Padding(4);
            this.inputLeft.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.inputLeft.Minimum = new decimal(new int[] {
            1000,
            0,
            0,
            -2147483648});
            this.inputLeft.Name = "inputLeft";
            this.inputLeft.Size = new System.Drawing.Size(160, 22);
            this.inputLeft.TabIndex = 3;
            this.inputLeft.Value = new decimal(new int[] {
            30,
            0,
            0,
            -2147483648});
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(15, 73);
            this.label2.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(160, 16);
            this.label2.TabIndex = 2;
            this.label2.Text = "Температура слева, °C:";
            // 
            // inputWidth
            // 
            this.inputWidth.DecimalPlaces = 3;
            this.inputWidth.Increment = new decimal(new int[] {
            1,
            0,
            0,
            196608});
            this.inputWidth.Location = new System.Drawing.Point(19, 41);
            this.inputWidth.Margin = new System.Windows.Forms.Padding(4);
            this.inputWidth.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            196608});
            this.inputWidth.Name = "inputWidth";
            this.inputWidth.Size = new System.Drawing.Size(160, 22);
            this.inputWidth.TabIndex = 1;
            this.inputWidth.Value = new decimal(new int[] {
            1,
            0,
            0,
            65536});
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(15, 21);
            this.label1.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(149, 16);
            this.label1.TabIndex = 0;
            this.label1.Text = "Толщина пластины, м:";
            // 
            // chart1
            // 
            this.chart1.BackColor = System.Drawing.Color.WhiteSmoke;
            chartArea1.AxisX.Maximum = 30D;
            chartArea1.AxisX.Minimum = 0D;
            chartArea1.AxisY.Maximum = 100D;
            chartArea1.AxisY.Minimum = -100D;
            chartArea1.Name = "ChartArea1";
            this.chart1.ChartAreas.Add(chartArea1);
            legend1.Name = "Legend1";
            this.chart1.Legends.Add(legend1);
            this.chart1.Location = new System.Drawing.Point(1, 241);
            this.chart1.Margin = new System.Windows.Forms.Padding(4);
            this.chart1.Name = "chart1";
            this.chart1.Palette = System.Windows.Forms.DataVisualization.Charting.ChartColorPalette.Bright;
            series1.ChartArea = "ChartArea1";
            series1.ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.Line;
            series1.Legend = "Legend1";
            series1.Name = "Series1";
            this.chart1.Series.Add(series1);
            this.chart1.Size = new System.Drawing.Size(784, 377);
            this.chart1.TabIndex = 1;
            this.chart1.Text = "chart1";
            // 
            // dataGridResults
            // 
            this.dataGridResults.BackgroundColor = System.Drawing.SystemColors.ActiveCaption;
            this.dataGridResults.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridResults.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.dtValue,
            this.h,
            this.Tmiddle,
            this.endTime});
            this.dataGridResults.GridColor = System.Drawing.SystemColors.WindowText;
            this.dataGridResults.Location = new System.Drawing.Point(1, 1);
            this.dataGridResults.Margin = new System.Windows.Forms.Padding(4);
            this.dataGridResults.Name = "dataGridResults";
            this.dataGridResults.RowHeadersWidth = 51;
            this.dataGridResults.Size = new System.Drawing.Size(784, 240);
            this.dataGridResults.TabIndex = 14;
            // 
            // dtValue
            // 
            this.dtValue.HeaderText = "Шаг по пространству";
            this.dtValue.MinimumWidth = 6;
            this.dtValue.Name = "dtValue";
            this.dtValue.Width = 125;
            // 
            // h
            // 
            this.h.HeaderText = "Шаг по времени";
            this.h.MinimumWidth = 6;
            this.h.Name = "h";
            this.h.Width = 125;
            // 
            // Tmiddle
            // 
            this.Tmiddle.HeaderText = "Температура в центральной точке";
            this.Tmiddle.MinimumWidth = 6;
            this.Tmiddle.Name = "Tmiddle";
            this.Tmiddle.Width = 125;
            // 
            // endTime
            // 
            this.endTime.HeaderText = "Время выполнения";
            this.endTime.MinimumWidth = 6;
            this.endTime.Name = "endTime";
            this.endTime.Width = 125;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ButtonShadow;
            this.ClientSize = new System.Drawing.Size(1067, 618);
            this.Controls.Add(this.dataGridResults);
            this.Controls.Add(this.chart1);
            this.Controls.Add(this.panel1);
            this.Margin = new System.Windows.Forms.Padding(4);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.inputStep)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputLambda)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputHeat)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputPlot)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputTime)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputDelta)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputStartTemp)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputRight)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputLeft)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.inputWidth)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.chart1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridResults)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.NumericUpDown inputWidth;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.DataVisualization.Charting.Chart chart1;
        private System.Windows.Forms.NumericUpDown inputRight;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.NumericUpDown inputLeft;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button btnStart;
        private System.Windows.Forms.NumericUpDown inputTime;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.NumericUpDown inputDelta;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.NumericUpDown inputStartTemp;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Button btnClear;
        private System.Windows.Forms.NumericUpDown inputLambda;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.NumericUpDown inputHeat;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.NumericUpDown inputPlot;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.DataGridView dataGridResults;
        private System.Windows.Forms.NumericUpDown inputStep;
        private System.Windows.Forms.Label label10;
        private System.Windows.Forms.DataGridViewTextBoxColumn dtValue;
        private System.Windows.Forms.DataGridViewTextBoxColumn h;
        private System.Windows.Forms.DataGridViewTextBoxColumn Tmiddle;
        private System.Windows.Forms.DataGridViewTextBoxColumn endTime;
    }
}