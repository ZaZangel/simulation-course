namespace Lab_3
{
    partial class Form1
    {
        private System.ComponentModel.IContainer components = null;

        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null)) components.Dispose();
            base.Dispose(disposing);
        }

        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.pbGrid = new System.Windows.Forms.PictureBox();
            this.timerSim = new System.Windows.Forms.Timer(this.components);
            this.btnStart = new System.Windows.Forms.Button();
            this.btnStop = new System.Windows.Forms.Button();
            this.btnReset = new System.Windows.Forms.Button();
            this.btnIgnite = new System.Windows.Forms.Button();
            this.btnIgniteRandom = new System.Windows.Forms.Button();
            this.btnAllRules = new System.Windows.Forms.Button();
            this.btnNoRules = new System.Windows.Forms.Button();
            this.groupBoxRules = new System.Windows.Forms.GroupBox();
            this.cbWind = new System.Windows.Forms.CheckBox();
            this.cbLightning = new System.Windows.Forms.CheckBox();
            this.cbBarrier = new System.Windows.Forms.CheckBox();
            this.cbHumidity = new System.Windows.Forms.CheckBox();
            this.lblStats = new System.Windows.Forms.Label();
            this.lblRules = new System.Windows.Forms.Label();
            this.lblTitle = new System.Windows.Forms.Label();
            this.groupBoxParams = new System.Windows.Forms.GroupBox();
            this.lblHumidity = new System.Windows.Forms.Label();
            this.trackHumidity = new System.Windows.Forms.TrackBar();
            this.lblHumidityValue = new System.Windows.Forms.Label();
            this.lblSpeed = new System.Windows.Forms.Label();
            this.trackSpeed = new System.Windows.Forms.TrackBar();
            this.lblSpeedValue = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.pbGrid)).BeginInit();
            this.groupBoxRules.SuspendLayout();
            this.groupBoxParams.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.trackHumidity)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackSpeed)).BeginInit();
            this.SuspendLayout();
            // 
            // pbGrid
            // 
            this.pbGrid.BackColor = System.Drawing.Color.Black;
            this.pbGrid.Location = new System.Drawing.Point(20, 60);
            this.pbGrid.Name = "pbGrid";
            this.pbGrid.Size = new System.Drawing.Size(500, 500);
            this.pbGrid.TabIndex = 0;
            this.pbGrid.TabStop = false;
            this.pbGrid.MouseClick += new System.Windows.Forms.MouseEventHandler(this.pbGrid_MouseClick);
            // 
            // timerSim
            // 
            this.timerSim.Interval = 150;
            // 
            // btnStart
            // 
            this.btnStart.Location = new System.Drawing.Point(540, 100);
            this.btnStart.Name = "btnStart";
            this.btnStart.Size = new System.Drawing.Size(130, 40);
            this.btnStart.TabIndex = 1;
            this.btnStart.Text = "▶ Старт";
            this.btnStart.Click += new System.EventHandler(this.btnStart_Click);
            // 
            // btnStop
            // 
            this.btnStop.Enabled = false;
            this.btnStop.Location = new System.Drawing.Point(540, 150);
            this.btnStop.Name = "btnStop";
            this.btnStop.Size = new System.Drawing.Size(130, 40);
            this.btnStop.TabIndex = 2;
            this.btnStop.Text = "⏹ Стоп";
            this.btnStop.Click += new System.EventHandler(this.btnStop_Click);
            // 
            // btnReset
            // 
            this.btnReset.Location = new System.Drawing.Point(540, 200);
            this.btnReset.Name = "btnReset";
            this.btnReset.Size = new System.Drawing.Size(130, 40);
            this.btnReset.TabIndex = 3;
            this.btnReset.Text = "🔄 Сброс";
            this.btnReset.Click += new System.EventHandler(this.btnReset_Click);
            // 
            // btnIgnite
            // 
            this.btnIgnite.Location = new System.Drawing.Point(540, 270);
            this.btnIgnite.Name = "btnIgnite";
            this.btnIgnite.Size = new System.Drawing.Size(130, 40);
            this.btnIgnite.TabIndex = 4;
            this.btnIgnite.Text = "🔥 Поджечь (центр)";
            this.btnIgnite.Click += new System.EventHandler(this.btnIgnite_Click);
            // 
            // btnIgniteRandom
            // 
            this.btnIgniteRandom.Location = new System.Drawing.Point(540, 320);
            this.btnIgniteRandom.Name = "btnIgniteRandom";
            this.btnIgniteRandom.Size = new System.Drawing.Size(130, 40);
            this.btnIgniteRandom.TabIndex = 5;
            this.btnIgniteRandom.Text = "🎲 Случайные очаги";
            this.btnIgniteRandom.Click += new System.EventHandler(this.btnIgniteRandom_Click);
            // 
            // btnAllRules
            // 
            this.btnAllRules.Location = new System.Drawing.Point(540, 380);
            this.btnAllRules.Name = "btnAllRules";
            this.btnAllRules.Size = new System.Drawing.Size(130, 35);
            this.btnAllRules.TabIndex = 6;
            this.btnAllRules.Text = "✅ Все правила";
            this.btnAllRules.Click += new System.EventHandler(this.btnAllRules_Click);
            // 
            // btnNoRules
            // 
            this.btnNoRules.Location = new System.Drawing.Point(540, 420);
            this.btnNoRules.Name = "btnNoRules";
            this.btnNoRules.Size = new System.Drawing.Size(130, 35);
            this.btnNoRules.TabIndex = 7;
            this.btnNoRules.Text = "⭕ Без правил";
            this.btnNoRules.Click += new System.EventHandler(this.btnNoRules_Click);
            // 
            // groupBoxRules
            // 
            this.groupBoxRules.Controls.Add(this.cbWind);
            this.groupBoxRules.Controls.Add(this.cbLightning);
            this.groupBoxRules.Controls.Add(this.cbBarrier);
            this.groupBoxRules.Controls.Add(this.cbHumidity);
            this.groupBoxRules.Location = new System.Drawing.Point(700, 60);
            this.groupBoxRules.Name = "groupBoxRules";
            this.groupBoxRules.Size = new System.Drawing.Size(280, 180);
            this.groupBoxRules.TabIndex = 8;
            this.groupBoxRules.TabStop = false;
            this.groupBoxRules.Text = "📋 Дополнительные правила";
            // 
            // cbWind
            // 
            this.cbWind.AutoSize = true;
            this.cbWind.Location = new System.Drawing.Point(15, 30);
            this.cbWind.Name = "cbWind";
            this.cbWind.Size = new System.Drawing.Size(158, 20);
            this.cbWind.TabIndex = 0;
            this.cbWind.Text = "🌬️ Ветерок (вправо)";
            this.cbWind.CheckedChanged += new System.EventHandler(this.Rule_CheckedChanged);
            // 
            // cbLightning
            // 
            this.cbLightning.AutoSize = true;
            this.cbLightning.Location = new System.Drawing.Point(15, 60);
            this.cbLightning.Name = "cbLightning";
            this.cbLightning.Size = new System.Drawing.Size(95, 20);
            this.cbLightning.TabIndex = 1;
            this.cbLightning.Text = "⚡ Молнии";
            this.cbLightning.CheckedChanged += new System.EventHandler(this.Rule_CheckedChanged);
            // 
            // cbBarrier
            // 
            this.cbBarrier.AutoSize = true;
            this.cbBarrier.Location = new System.Drawing.Point(15, 90);
            this.cbBarrier.Name = "cbBarrier";
            this.cbBarrier.Size = new System.Drawing.Size(149, 20);
            this.cbBarrier.TabIndex = 2;
            this.cbBarrier.Text = "🌊 Река (преграда)";
            this.cbBarrier.CheckedChanged += new System.EventHandler(this.Rule_CheckedChanged);
            // 
            // cbHumidity
            // 
            this.cbHumidity.AutoSize = true;
            this.cbHumidity.Location = new System.Drawing.Point(15, 120);
            this.cbHumidity.Name = "cbHumidity";
            this.cbHumidity.Size = new System.Drawing.Size(115, 20);
            this.cbHumidity.TabIndex = 3;
            this.cbHumidity.Text = "💧 Влажность";
            this.cbHumidity.CheckedChanged += new System.EventHandler(this.Rule_CheckedChanged);
            // 
            // lblStats
            // 
            this.lblStats.BackColor = System.Drawing.Color.White;
            this.lblStats.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.lblStats.Location = new System.Drawing.Point(20, 570);
            this.lblStats.Name = "lblStats";
            this.lblStats.Padding = new System.Windows.Forms.Padding(5);
            this.lblStats.Size = new System.Drawing.Size(200, 80);
            this.lblStats.TabIndex = 10;
            // 
            // lblRules
            // 
            this.lblRules.BackColor = System.Drawing.Color.White;
            this.lblRules.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.lblRules.Font = new System.Drawing.Font("Segoe UI", 9F);
            this.lblRules.Location = new System.Drawing.Point(700, 410);
            this.lblRules.Name = "lblRules";
            this.lblRules.Padding = new System.Windows.Forms.Padding(5);
            this.lblRules.Size = new System.Drawing.Size(280, 240);
            this.lblRules.TabIndex = 11;
            // 
            // lblTitle
            // 
            this.lblTitle.AutoSize = true;
            this.lblTitle.Font = new System.Drawing.Font("Segoe UI", 14F, System.Drawing.FontStyle.Bold);
            this.lblTitle.Location = new System.Drawing.Point(20, 15);
            this.lblTitle.Name = "lblTitle";
            this.lblTitle.Size = new System.Drawing.Size(492, 32);
            this.lblTitle.TabIndex = 0;
            this.lblTitle.Text = "🌲🔥 Моделирование лесных пожаров";
            // 
            // groupBoxParams
            // 
            this.groupBoxParams.Controls.Add(this.lblHumidity);
            this.groupBoxParams.Controls.Add(this.trackHumidity);
            this.groupBoxParams.Controls.Add(this.lblHumidityValue);
            this.groupBoxParams.Controls.Add(this.lblSpeed);
            this.groupBoxParams.Controls.Add(this.trackSpeed);
            this.groupBoxParams.Controls.Add(this.lblSpeedValue);
            this.groupBoxParams.Location = new System.Drawing.Point(700, 250);
            this.groupBoxParams.Name = "groupBoxParams";
            this.groupBoxParams.Size = new System.Drawing.Size(280, 150);
            this.groupBoxParams.TabIndex = 9;
            this.groupBoxParams.TabStop = false;
            this.groupBoxParams.Text = "⚙️ Параметры";
            // 
            // lblHumidity
            // 
            this.lblHumidity.AutoSize = true;
            this.lblHumidity.Location = new System.Drawing.Point(15, 30);
            this.lblHumidity.Name = "lblHumidity";
            this.lblHumidity.Size = new System.Drawing.Size(81, 16);
            this.lblHumidity.TabIndex = 0;
            this.lblHumidity.Text = "Влажность:";
            // 
            // trackHumidity
            // 
            this.trackHumidity.Location = new System.Drawing.Point(90, 25);
            this.trackHumidity.Maximum = 100;
            this.trackHumidity.Name = "trackHumidity";
            this.trackHumidity.Size = new System.Drawing.Size(130, 56);
            this.trackHumidity.TabIndex = 1;
            this.trackHumidity.Value = 50;
            this.trackHumidity.Scroll += new System.EventHandler(this.trackHumidity_Scroll);
            // 
            // lblHumidityValue
            // 
            this.lblHumidityValue.AutoSize = true;
            this.lblHumidityValue.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Bold);
            this.lblHumidityValue.Location = new System.Drawing.Point(230, 30);
            this.lblHumidityValue.Name = "lblHumidityValue";
            this.lblHumidityValue.Size = new System.Drawing.Size(40, 18);
            this.lblHumidityValue.TabIndex = 2;
            this.lblHumidityValue.Text = "50%";
            // 
            // lblSpeed
            // 
            this.lblSpeed.AutoSize = true;
            this.lblSpeed.Location = new System.Drawing.Point(15, 70);
            this.lblSpeed.Name = "lblSpeed";
            this.lblSpeed.Size = new System.Drawing.Size(71, 16);
            this.lblSpeed.TabIndex = 3;
            this.lblSpeed.Text = "Скорость:";
            // 
            // trackSpeed
            // 
            this.trackSpeed.Location = new System.Drawing.Point(90, 65);
            this.trackSpeed.Minimum = 1;
            this.trackSpeed.Name = "trackSpeed";
            this.trackSpeed.Size = new System.Drawing.Size(130, 56);
            this.trackSpeed.TabIndex = 4;
            this.trackSpeed.Value = 5;
            this.trackSpeed.Scroll += new System.EventHandler(this.trackSpeed_Scroll);
            // 
            // lblSpeedValue
            // 
            this.lblSpeedValue.AutoSize = true;
            this.lblSpeedValue.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Bold);
            this.lblSpeedValue.Location = new System.Drawing.Point(230, 70);
            this.lblSpeedValue.Name = "lblSpeedValue";
            this.lblSpeedValue.Size = new System.Drawing.Size(25, 18);
            this.lblSpeedValue.TabIndex = 5;
            this.lblSpeedValue.Text = "5x";
            // 
            // Form1
            // 
            this.BackColor = System.Drawing.Color.LightGray;
            this.ClientSize = new System.Drawing.Size(1002, 653);
            this.Controls.Add(this.lblTitle);
            this.Controls.Add(this.pbGrid);
            this.Controls.Add(this.btnStart);
            this.Controls.Add(this.btnStop);
            this.Controls.Add(this.btnReset);
            this.Controls.Add(this.btnIgnite);
            this.Controls.Add(this.btnIgniteRandom);
            this.Controls.Add(this.btnAllRules);
            this.Controls.Add(this.btnNoRules);
            this.Controls.Add(this.groupBoxRules);
            this.Controls.Add(this.groupBoxParams);
            this.Controls.Add(this.lblStats);
            this.Controls.Add(this.lblRules);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.MaximizeBox = false;
            this.Name = "Form1";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Лабораторная №3: Лесные пожары";
            ((System.ComponentModel.ISupportInitialize)(this.pbGrid)).EndInit();
            this.groupBoxRules.ResumeLayout(false);
            this.groupBoxRules.PerformLayout();
            this.groupBoxParams.ResumeLayout(false);
            this.groupBoxParams.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.trackHumidity)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.trackSpeed)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        private System.Windows.Forms.PictureBox pbGrid;
        private System.Windows.Forms.Timer timerSim;
        private System.Windows.Forms.Button btnStart, btnStop, btnReset, btnIgnite, btnIgniteRandom;
        private System.Windows.Forms.Button btnAllRules, btnNoRules;
        private System.Windows.Forms.GroupBox groupBoxRules, groupBoxParams;
        private System.Windows.Forms.CheckBox cbWind, cbLightning, cbBarrier, cbHumidity;
        private System.Windows.Forms.Label lblStats, lblRules, lblTitle, lblHumidity, lblHumidityValue, lblSpeed, lblSpeedValue;
        private System.Windows.Forms.TrackBar trackHumidity, trackSpeed;
    }
}