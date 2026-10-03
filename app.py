import streamlit as st

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Electromagnetic Spectrum Educational App",
    page_icon="🌈",
    layout="wide"
)

# ============================================================
# CONSTANTS
# ============================================================

SPEED_OF_LIGHT = 3.0e8
PLANCK_CONSTANT = 6.626e-34

# ============================================================
# SESSION STATE
# ============================================================

if "completed_sections" not in st.session_state:
    st.session_state.completed_sections = set()

if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0

if "quiz_percentage" not in st.session_state:
    st.session_state.quiz_percentage = 0

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main-title {
    font-size: 42px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 10px;
}

.subtitle {
    font-size: 20px;
    text-align: center;
    margin-bottom: 30px;
}

/* HOME PAGE CARDS */

.card {
    padding: 24px;
    border-radius: 15px;
    background-color: #ffffff;
    color: #222222;
    margin-bottom: 15px;
    border: 1px solid #dddddd;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    min-height: 160px;
}

.card h3 {
    color: #222222 !important;
    margin-bottom: 10px;
}

.card p {
    color: #555555 !important;
    line-height: 1.6;
}

/* FORMULA BOX */

.formula {
    padding: 15px;
    border-radius: 12px;
    background-color: #eeeeee;
    color: #222222;
    text-align: center;
    font-size: 25px;
    font-weight: bold;
    margin: 15px 0;
}

/* FOOTER */

.footer {
    text-align: center;
    margin-top: 40px;
    padding: 20px;
    color: gray;
}

/* SECTION BOX */

.info-box {
    padding: 20px;
    border-radius: 15px;
    background-color: #f5f5f5;
    color: #222222;
    margin: 15px 0;
}

/* MOBILE */

@media (max-width: 768px) {
    .main-title {
        font-size: 30px;
    }

    .subtitle {
        font-size: 17px;
    }

    .card {
        min-height: auto;
    }
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# ELECTROMAGNETIC SPECTRUM DATA
# ============================================================

spectrum = {

    "Radio Waves": {
        "wavelength": "> 1 m",
        "frequency": "< 300 MHz",
        "energy": "Lowest",
        "source": "Antennas and electrical circuits",
        "uses": "Radio, TV broadcasting, communication",
        "advantages": "Long-distance communication",
        "risks": "Generally low risk at normal exposure levels",
        "example": "Radio broadcasting"
    },

    "Microwaves": {
        "wavelength": "1 mm – 1 m",
        "frequency": "300 MHz – 300 GHz",
        "energy": "Low",
        "source": "Electronic oscillators and transmitters",
        "uses": "Wi-Fi, radar, satellite communication, microwave ovens",
        "advantages": "Wireless communication and radar",
        "risks": "High exposure can cause heating",
        "example": "Wi-Fi"
    },

    "Infrared": {
        "wavelength": "700 nm – 1 mm",
        "frequency": "300 GHz – 430 THz",
        "energy": "Low-Medium",
        "source": "Warm and hot objects",
        "uses": "Remote controls, thermal cameras, heat sensors",
        "advantages": "Thermal imaging and sensing",
        "risks": "Strong exposure can heat tissue",
        "example": "TV remote"
    },

    "Visible Light": {
        "wavelength": "380 – 750 nm",
        "frequency": "430 – 790 THz",
        "energy": "Medium",
        "source": "Sun, lamps and LEDs",
        "uses": "Vision, lighting, photography, optical instruments",
        "advantages": "Allows human vision",
        "risks": "Very bright light can damage eyes",
        "example": "Sunlight"
    },

    "Ultraviolet": {
        "wavelength": "10 – 400 nm",
        "frequency": "750 THz – 30 PHz",
        "energy": "High",
        "source": "Sun and UV lamps",
        "uses": "Sterilization, security marking, medical applications",
        "advantages": "Disinfection and scientific applications",
        "risks": "Can damage skin and eyes",
        "example": "UV sterilization"
    },

    "X-rays": {
        "wavelength": "0.01 – 10 nm",
        "frequency": "30 PHz – 30 EHz",
        "energy": "Very High",
        "source": "X-ray tubes and high-energy processes",
        "uses": "Medical imaging, security scanning",
        "advantages": "Can image internal structures",
        "risks": "Ionizing radiation can damage cells",
        "example": "Medical X-ray"
    },

    "Gamma Rays": {
        "wavelength": "< 0.01 nm",
        "frequency": "> 30 EHz",
        "energy": "Highest",
        "source": "Nuclear reactions and radioactive decay",
        "uses": "Cancer treatment, sterilization, astronomy",
        "advantages": "Medical treatment and scientific research",
        "risks": "Highly penetrating ionizing radiation",
        "example": "Radiotherapy"
    }
}

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🌈 EM Spectrum")

st.sidebar.markdown("---")

st.sidebar.subheader("📊 Your Progress")

completed = len(st.session_state.completed_sections)

total_sections = 7

progress = completed / total_sections

if progress > 1:
    progress = 1

st.sidebar.progress(progress)

st.sidebar.write(
    f"Completed: {completed}/{total_sections}"
)

if st.session_state.quiz_percentage > 0:
    st.sidebar.write(
        f"Quiz: {st.session_state.quiz_percentage:.0f}%"
    )

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Choose a section:",
    [
        "🏠 Home",
        "🔬 Explore Spectrum",
        "🌈 Visible Light",
        "🌊 Wave Diagrams",
        "📊 Comparison",
        "📈 Relationships",
        "🧮 Wave Calculator",
        "📝 Quiz",
        "📊 My Progress",
        "ℹ️ About Project"
    ]
)

# ============================================================
# HOME
# ============================================================

if page == "🏠 Home":

    st.markdown(
        '<div class="main-title">🌈 Electromagnetic Spectrum</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Interactive Educational App</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Welcome to the Electromagnetic Spectrum Educational App!"
    )

    st.write(
        "This application helps students understand electromagnetic "
        "waves, their properties, applications, relationships and energy."
    )

    st.markdown("---")

    # THREE FEATURE CARDS

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
            <div class="card">
                <h3>🔬 Explore</h3>
                <p>
                Explore all seven regions of the electromagnetic spectrum.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="card">
                <h3>🧮 Calculate</h3>
                <p>
                Calculate frequency and photon energy from wavelength.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            """
            <div class="card">
                <h3>📝 Test Yourself</h3>
                <p>
                Take the interactive quiz and check your understanding.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # SPECTRUM

    st.markdown("## 🌈 Electromagnetic Spectrum")

    st.markdown(
        """
        <div style="
        display:flex;
        height:80px;
        border-radius:12px;
        overflow:hidden;
        margin:20px 0;
        ">

        <div style="
        flex:1;
        background:#555;
        color:white;
        display:flex;
        align-items:center;
        justify-content:center;">
        Radio
        </div>

        <div style="
        flex:1;
        background:#666;
        color:white;
        display:flex;
        align-items:center;
        justify-content:center;">
        Microwave
        </div>

        <div style="
        flex:1;
        background:#777;
        color:white;
        display:flex;
        align-items:center;
        justify-content:center;">
        Infrared
        </div>

        <div style="
        flex:1;
        background:#888;
        color:white;
        display:flex;
        align-items:center;
        justify-content:center;">
        Visible
        </div>

        <div style="
        flex:1;
        background:#999;
        color:white;
        display:flex;
        align-items:center;
        justify-content:center;">
        UV
        </div>

        <div style="
        flex:1;
        background:#aaa;
        color:black;
        display:flex;
        align-items:center;
        justify-content:center;">
        X-Ray
        </div>

        <div style="
        flex:1;
        background:#ccc;
        color:black;
        display:flex;
        align-items:center;
        justify-content:center;">
        Gamma
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### Important Relationships")

    st.markdown(
        """
        **Speed of light:**

        c = fλ

        **Photon energy:**

        E = hf

        Where:

        - c = speed of light
        - f = frequency
        - λ = wavelength
        - E = photon energy
        - h = Planck's constant
        """
    )

    st.markdown("## 📚 Seven Regions")

    for region in spectrum:
        st.write(f"🔹 **{region}**")


# ============================================================
# EXPLORE SPECTRUM
# ============================================================

elif page == "🔬 Explore Spectrum":

    st.markdown(
        '<div class="main-title">🔬 Explore the Spectrum</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Select a region to learn about its wavelength, frequency, "
        "energy, uses and safety considerations."
    )

    st.markdown("## 🌈 Spectrum")

    st.markdown(
        """
        <div style="
        display:flex;
        height:70px;
        border-radius:12px;
        overflow:hidden;
        ">

        <div style="flex:1;background:#555;color:white;
        display:flex;align-items:center;justify-content:center;">
        Radio
        </div>

        <div style="flex:1;background:#666;color:white;
        display:flex;align-items:center;justify-content:center;">
        Microwave
        </div>

        <div style="flex:1;background:#777;color:white;
        display:flex;align-items:center;justify-content:center;">
        Infrared
        </div>

        <div style="flex:1;background:#888;color:white;
        display:flex;align-items:center;justify-content:center;">
        Visible
        </div>

        <div style="flex:1;background:#999;color:white;
        display:flex;align-items:center;justify-content:center;">
        UV
        </div>

        <div style="flex:1;background:#aaa;color:black;
        display:flex;align-items:center;justify-content:center;">
        X-Ray
        </div>

        <div style="flex:1;background:#ccc;color:black;
        display:flex;align-items:center;justify-content:center;">
        Gamma
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.info(
        "Moving from Radio Waves to Gamma Rays: "
        "wavelength decreases while frequency and photon energy increase."
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### 📏 Wavelength")

        st.write(
            "Wavelength is the distance between corresponding "
            "points of consecutive waves."
        )

    with col2:

        st.markdown("### 🔄 Frequency")

        st.write(
            "Frequency represents the number of wave cycles "
            "passing a point per second."
        )

    region = st.selectbox(
        "Select an electromagnetic region:",
        list(spectrum.keys())
    )

    data = spectrum[region]

    st.markdown("---")

    st.markdown(f"## 🌟 {region}")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "📏 Wavelength",
            data["wavelength"]
        )

    with col2:
        st.metric(
            "🔄 Frequency",
            data["frequency"]
        )

    with col3:
        st.metric(
            "⚡ Energy",
            data["energy"]
        )

    st.markdown("### 🔬 Source")
    st.write(data["source"])

    st.markdown("### 🛠️ Uses")
    st.write(data["uses"])

    st.markdown("### 💡 Example")
    st.write(data["example"])

    st.markdown("### ✅ Advantages")
    st.write(data["advantages"])

    st.markdown("### ⚠️ Risks")
    st.write(data["risks"])

    st.markdown("## 📐 Important Formula")

    st.markdown(
        '<div class="formula">c = fλ</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="formula">E = hf</div>',
        unsafe_allow_html=True
    )

    st.session_state.completed_sections.add(
        "Explore Spectrum"
    )


# ============================================================
# VISIBLE LIGHT
# ============================================================

elif page == "🌈 Visible Light":

    st.markdown(
        '<div class="main-title">🌈 Visible Light</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Visible light is the portion of the electromagnetic "
        "spectrum that can be detected by the human eye."
    )

    st.markdown("## 🌈 Visible Light Colors")

    colors = [
        ("Violet", "380–450 nm"),
        ("Blue", "450–495 nm"),
        ("Green", "495–570 nm"),
        ("Yellow", "570–590 nm"),
        ("Orange", "590–620 nm"),
        ("Red", "620–750 nm")
    ]

    for color, wavelength in colors:

        st.markdown(
            f"""
            <div style="
            padding:15px;
            margin:8px 0;
            border-radius:10px;
            background:#f2f2f2;
            text-align:center;
            font-size:20px;
            color:#222;
            ">

            <b>{color}</b>
            <br>
            <small>{wavelength}</small>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("## 👁️ Human Vision")

    st.write(
        "The human eye detects approximately "
        "380 nm to 750 nm of the electromagnetic spectrum."
    )

    st.info(
        "Violet has a shorter wavelength and higher frequency "
        "than red light."
    )

    st.markdown("## 🔬 Applications")

    st.write("• Human vision")
    st.write("• Photography")
    st.write("• Optical communication")
    st.write("• Lighting")
    st.write("• Microscopy")

    st.session_state.completed_sections.add(
        "Visible Light"
    )


# ============================================================
# WAVE DIAGRAMS
# ============================================================

elif page == "🌊 Wave Diagrams":

    st.markdown(
        '<div class="main-title">🌊 Wave Diagrams</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Visualize wavelength, frequency and energy relationships'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("## 1️⃣ Understanding Wavelength")

    st.info(
        "Wavelength (λ) is the distance between two consecutive "
        "corresponding points of a wave."
    )

    st.markdown(
        """
        <div style="
        background:#f5f5f5;
        padding:30px;
        border-radius:15px;
        text-align:center;
        font-size:30px;
        color:#222;
        ">

        🌊〰️〰️〰️〰️〰️🌊

        <br><br>

        <span style="font-size:18px;">
        ←──── Wavelength (λ) ────→
        </span>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## 2️⃣ Low Frequency vs High Frequency")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🔵 Low Frequency")

        st.markdown(
            """
            <div style="
            background:#e8f4ff;
            padding:25px;
            border-radius:15px;
            text-align:center;
            font-size:25px;
            color:#222;
            ">

            〰️　　　〰️　　　〰️

            <br><br>

            <small>Fewer wave cycles</small>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("• Longer wavelength")
        st.write("• Lower frequency")
        st.write("• Lower energy")

    with col2:

        st.subheader("🔴 High Frequency")

        st.markdown(
            """
            <div style="
            background:#fff0f0;
            padding:25px;
            border-radius:15px;
            text-align:center;
            font-size:25px;
            color:#222;
            ">

            〰️〰️〰️〰️〰️〰️

            <br><br>

            <small>More wave cycles</small>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("• Shorter wavelength")
        st.write("• Higher frequency")
        st.write("• Higher energy")

    st.markdown("## 3️⃣ Electromagnetic Spectrum Direction")

    st.markdown(
        """
        <div style="
        padding:25px;
        border-radius:15px;
        background:linear-gradient(
        90deg,
        #eeeeee,
        #dddddd,
        #bbbbbb,
        #999999,
        #777777,
        #555555,
        #333333);
        color:white;
        text-align:center;
        font-weight:bold;
        ">

        RADIO → MICROWAVE → INFRARED →
        VISIBLE → UV → X-RAY → GAMMA

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "📏 Wavelength",
            "Decreases →"
        )

    with col2:
        st.metric(
            "🔄 Frequency",
            "Increases →"
        )

    with col3:
        st.metric(
            "⚡ Energy",
            "Increases →"
        )

    st.markdown("## 4️⃣ Important Relationships")

    st.markdown(
        '<div class="formula">c = fλ</div>',
        unsafe_allow_html=True
    )

    st.write(
        "For electromagnetic waves in vacuum, the speed of light "
        "is approximately constant. Therefore, wavelength and "
        "frequency have an inverse relationship."
    )

    st.markdown(
        '<div class="formula">E = hf</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Photon energy increases with frequency."
    )

    st.markdown("## 🧠 Remember")

    st.success(
        """
        Longer wavelength → Lower frequency → Lower energy

        Shorter wavelength → Higher frequency → Higher energy
        """
    )

    st.session_state.completed_sections.add(
        "Wave Diagrams"
    )


# ============================================================
# COMPARISON
# ============================================================

elif page == "📊 Comparison":

    st.markdown(
        '<div class="main-title">📊 Spectrum Comparison</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Compare the seven regions of the electromagnetic spectrum."
    )

    for region, data in spectrum.items():

        with st.expander(f"🌟 {region}"):

            col1, col2, col3 = st.columns(3)

            with col1:
                st.write(
                    f"📏 **Wavelength:** {data['wavelength']}"
                )

            with col2:
                st.write(
                    f"🔄 **Frequency:** {data['frequency']}"
                )

            with col3:
                st.write(
                    f"⚡ **Energy:** {data['energy']}"
                )

            st.write(
                f"🛠️ **Uses:** {data['uses']}"
            )

            st.write(
                f"💡 **Example:** {data['example']}"
            )

            st.write(
                f"⚠️ **Risks:** {data['risks']}"
            )

    st.session_state.completed_sections.add(
        "Comparison"
    )


# ============================================================
# RELATIONSHIPS
# ============================================================

elif page == "📈 Relationships":

    st.markdown(
        '<div class="main-title">📈 Wave Relationships</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Change the wavelength and observe how frequency "
        "and photon energy change."
    )

    wavelength_log = st.slider(
        "Select wavelength on a logarithmic scale",
        min_value=-12.0,
        max_value=3.0,
        value=-6.0,
        step=0.1
    )

    wavelength = 10 ** wavelength_log

    frequency = SPEED_OF_LIGHT / wavelength

    energy = PLANCK_CONSTANT * frequency

    st.markdown("## 📊 Calculated Values")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "📏 Wavelength",
            f"{wavelength:.3e} m"
        )

    with col2:
        st.metric(
            "🔄 Frequency",
            f"{frequency:.3e} Hz"
        )

    with col3:
        st.metric(
            "⚡ Photon Energy",
            f"{energy:.3e} J"
        )

    st.markdown("## 📐 Formulas")

    st.markdown(
        '<div class="formula">c = fλ</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="formula">E = hf</div>',
        unsafe_allow_html=True
    )

    # Determine region

    if wavelength > 1:

        region = "Radio Waves"

    elif wavelength > 1e-3:

        region = "Microwaves"

    elif wavelength > 7e-7:

        region = "Infrared"

    elif wavelength > 3.8e-7:

        region = "Visible Light"

    elif wavelength > 1e-8:

        region = "Ultraviolet"

    elif wavelength > 1e-11:

        region = "X-rays"

    else:

        region = "Gamma Rays"

    st.success(
        f"Approximate region: **{region}**"
    )

    st.session_state.completed_sections.add(
        "Relationships"
    )


# ============================================================
# WAVE CALCULATOR
# ============================================================

elif page == "🧮 Wave Calculator":

    st.markdown(
        '<div class="main-title">🧮 Wave Calculator</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Enter a wavelength and calculate frequency "
        "and photon energy."
    )

    wavelength_input = st.number_input(
        "Enter wavelength",
        min_value=0.000000000001,
        value=500.0,
        format="%.6f"
    )

    unit = st.selectbox(
        "Select unit",
        ["m", "cm", "mm", "µm", "nm"]
    )

    conversion = {
        "m": 1,
        "cm": 1e-2,
        "mm": 1e-3,
        "µm": 1e-6,
        "nm": 1e-9
    }

    wavelength_m = (
        wavelength_input *
        conversion[unit]
    )

    frequency = (
        SPEED_OF_LIGHT /
        wavelength_m
    )

    energy = (
        PLANCK_CONSTANT *
        frequency
    )

    st.markdown("---")

    st.markdown("## 📊 Results")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "📏 Wavelength",
            f"{wavelength_m:.3e} m"
        )

    with col2:

        st.metric(
            "🔄 Frequency",
            f"{frequency:.3e} Hz"
        )

    with col3:

        st.metric(
            "⚡ Photon Energy",
            f"{energy:.3e} J"
        )

    # Determine region

    if wavelength_m > 1:

        region = "Radio Waves"

    elif wavelength_m > 1e-3:

        region = "Microwaves"

    elif wavelength_m > 7e-7:

        region = "Infrared"

    elif wavelength_m >= 3.8e-7:

        region = "Visible Light"

    elif wavelength_m > 1e-8:

        region = "Ultraviolet"

    elif wavelength_m > 1e-11:

        region = "X-rays"

    else:

        region = "Gamma Rays"

    st.success(
        f"🌈 Approximate EM region: **{region}**"
    )

    st.markdown("## 📐 Formulas Used")

    st.markdown(
        '<div class="formula">f = c / λ</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="formula">E = hf</div>',
        unsafe_allow_html=True
    )

    st.write("**c** = 3 × 10⁸ m/s")

    st.write("**h** = 6.626 × 10⁻³⁴ J·s")

    st.session_state.completed_sections.add(
        "Wave Calculator"
    )


# ============================================================
# QUIZ
# ============================================================

elif page == "📝 Quiz":

    st.markdown(
        '<div class="main-title">'
        '📝 Electromagnetic Spectrum Quiz'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Answer the following questions and calculate your score."
    )

    questions = [

        (
            "Which electromagnetic wave has the longest wavelength?",
            [
                "Gamma Rays",
                "X-rays",
                "Radio Waves",
                "Ultraviolet"
            ],
            "Radio Waves"
        ),

        (
            "Which electromagnetic wave has the highest frequency?",
            [
                "Radio Waves",
                "Microwaves",
                "Visible Light",
                "Gamma Rays"
            ],
            "Gamma Rays"
        ),

        (
            "Which electromagnetic radiation is used in TV remote controls?",
            [
                "Infrared",
                "Gamma Rays",
                "X-rays",
                "Radio Waves"
            ],
            "Infrared"
        ),

        (
            "Which radiation is commonly used for medical imaging?",
            [
                "Radio Waves",
                "X-rays",
                "Microwaves",
                "Infrared"
            ],
            "X-rays"
        ),

        (
            "Which electromagnetic waves are visible to the human eye?",
            [
                "Radio Waves",
                "Visible Light",
                "Gamma Rays",
                "X-rays"
            ],
            "Visible Light"
        ),

        (
            "Which equation relates speed, frequency and wavelength?",
            [
                "E = mc²",
                "c = fλ",
                "F = ma",
                "P = VI"
            ],
            "c = fλ"
        ),

        (
            "What happens to frequency when wavelength decreases?",
            [
                "It decreases",
                "It increases",
                "It becomes zero",
                "It remains unchanged"
            ],
            "It increases"
        ),

        (
            "Which radiation has the highest photon energy?",
            [
                "Infrared",
                "Visible Light",
                "Gamma Rays",
                "Microwaves"
            ],
            "Gamma Rays"
        ),

        (
            "Which electromagnetic waves are commonly associated with heating?",
            [
                "Infrared",
                "Gamma Rays",
                "X-rays",
                "Ultraviolet"
            ],
            "Infrared"
        ),

        (
            "What is the approximate speed of electromagnetic waves in vacuum?",
            [
                "3 × 10⁶ m/s",
                "3 × 10⁷ m/s",
                "3 × 10⁸ m/s",
                "3 × 10⁹ m/s"
            ],
            "3 × 10⁸ m/s"
        )
    ]

    answers = []

    for i, (question, options, correct) in enumerate(questions):

        st.markdown(
            f"### {i + 1}. {question}"
        )

        answer = st.radio(
            "Choose an answer:",
            options,
            key=f"question_{i}"
        )

        answers.append(answer)

    if st.button("Calculate Score"):

        score = 0

        for i, (_, _, correct) in enumerate(questions):

            if answers[i] == correct:
                score += 1

        percentage = (
            score / len(questions)
        ) * 100

        st.session_state.quiz_score = score

        st.session_state.quiz_percentage = percentage

        st.session_state.completed_sections.add(
            "Quiz"
        )

        st.markdown("---")

        st.success(
            f"🎉 Your score: "
            f"{score}/{len(questions)}"
        )

        st.info(
            f"📊 Percentage: "
            f"{percentage:.0f}%"
        )

        if percentage == 100:

            st.balloons()

            st.success(
                "Excellent! You answered every "
                "question correctly."
            )

        elif percentage >= 70:

            st.success(
                "Good job! Keep practicing "
                "to improve further."
            )

        elif percentage >= 50:

            st.warning(
                "You have a basic understanding. "
                "Review the spectrum sections."
            )

        else:

            st.error(
                "Review the learning sections "
                "and try the quiz again."
            )


# ============================================================
# MY PROGRESS
# ============================================================

elif page == "📊 My Progress":

    st.markdown(
        '<div class="main-title">📊 My Progress</div>',
        unsafe_allow_html=True
    )

    completed = len(
        st.session_state.completed_sections
    )

    total = 7

    progress = completed / total

    if progress > 1:
        progress = 1

    st.progress(progress)

    st.write(
        f"### Completed Activities: "
        f"{completed}/{total}"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "📚 Activities",
            f"{completed}/{total}"
        )

    with col2:

        st.metric(
            "📝 Quiz Score",
            f"{st.session_state.quiz_score}/10"
        )

    with col3:

        st.metric(
            "📈 Quiz %",
            f"{st.session_state.quiz_percentage:.0f}%"
        )

    st.markdown("---")

    st.markdown("## ✅ Completed Sections")

    if completed == 0:

        st.info(
            "Start exploring the application "
            "to track your progress."
        )

    else:

        for section in st.session_state.completed_sections:

            st.success(
                f"✅ {section}"
            )

    if completed == total:

        st.balloons()

        st.success(
            "🎉 Congratulations! You completed "
            "all learning activities."
        )

    st.markdown("---")

    if st.button("🔄 Reset Progress"):

        st.session_state.completed_sections = set()

        st.session_state.quiz_score = 0

        st.session_state.quiz_percentage = 0

        st.rerun()


# ============================================================
# ABOUT PROJECT
# ============================================================

elif page == "ℹ️ About Project":

    st.markdown(
        '<div class="main-title">ℹ️ About the Project</div>',
        unsafe_allow_html=True
    )

    st.write(
        "The Electromagnetic Spectrum Educational App "
        "is an interactive educational application designed "
        "to help students understand electromagnetic radiation."
    )

    st.markdown("## 🎯 Objective")

    st.write(
        "The main objective is to provide an interactive "
        "and easy-to-understand platform for learning "
        "the electromagnetic spectrum."
    )

    st.markdown("## 🛠️ Technologies Used")

    st.write("🐍 Python")

    st.write("🎈 Streamlit")

    st.write("🧮 Mathematical calculations")

    st.write("🎨 HTML/CSS for interface design")

    st.markdown("## 📚 Topics Covered")

    st.write("• Electromagnetic spectrum")

    st.write("• Wavelength")

    st.write("• Frequency")

    st.write("• Photon energy")

    st.write("• Visible light")

    st.write("• Applications of EM waves")

    st.write("• Safety considerations")

    st.write("• Wave relationships")

    st.write("• Numerical calculations")

    st.write("• Interactive quiz")

    st.markdown("## 🧮 Calculations")

    st.write(
        "The application calculates frequency using:"
    )

    st.markdown(
        '<div class="formula">f = c / λ</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Photon energy is calculated using:"
    )

    st.markdown(
        '<div class="formula">E = hf</div>',
        unsafe_allow_html=True
    )

    st.markdown("## 🚀 Future Enhancements")

    st.write("• More animations")

    st.write("• Interactive graphs")

    st.write("• More quizzes")

    st.write("• User accounts")

    st.write("• Database-based progress tracking")

    st.write("• Mobile-friendly interface")


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

    🌈 Electromagnetic Spectrum Educational App

    <br>

    Built using Python & Streamlit

    <br><br>

    Educational Project

    </div>
    """,
    unsafe_allow_html=True
)