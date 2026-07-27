<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>3D Animated বিবাহের বায়োডাটা - মোঃ ওমর হানিফ</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Anek+Bangla:wght@400;500;600;700;800&family=Noto+Sans+Bengali:wght@400;500;600;700&family=Great+Vibes&display=swap');

        :root {
            --bg-body: #e2e8f0;
            --card-3d-bg: #ffffff;
            --primary-dark: #1e293b;
            --primary-dark-light: #334155;
            --accent-mint: #14b8a6;
            --accent-mint-soft: #ccfbf1;
            --text-main: #0f172a;
            --text-muted: #475569;
            
            --shadow-3d-large: 0 25px 35px -5px rgba(0, 0, 0, 0.25), 0 10px 15px -6px rgba(0, 0, 0, 0.15);
            --shadow-3d-box: 0 10px 20px -3px rgba(0, 0, 0, 0.1), 0 4px 8px -4px rgba(0, 0, 0, 0.06);
            --shadow-button-3d: 0 5px 0px #0d9488, 0 8px 15px rgba(0,0,0,0.2);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            -webkit-tap-highlight-color: transparent;
        }

        body {
            font-family: 'Anek Bangla', 'Noto Sans Bengali', sans-serif;
            background: linear-gradient(135deg, #cbd5e1 0%, #f1f5f9 100%);
            display: flex;
            justify-content: center;
            padding: 20px 10px;
            color: var(--text-main);
            line-height: 1.6;
            perspective: 1200px;
            overflow-x: hidden;
        }

        .resume-container {
            width: 100%;
            max-width: 880px;
            background-color: var(--card-3d-bg);
            border-radius: 20px;
            box-shadow: var(--shadow-3d-large);
            display: flex;
            flex-direction: column;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.9);
            animation: container3DEntrance 1s cubic-bezier(0.16, 1, 0.3, 1) forwards;
            transform-style: preserve-3d;
            transition: transform 0.4s ease, box-shadow 0.4s ease;
        }

        @keyframes container3DEntrance {
            0% {
                opacity: 0;
                transform: translateY(50px) scale(0.92) rotateX(10deg);
            }
            100% {
                opacity: 1;
                transform: translateY(0) scale(1) rotateX(0deg);
            }
        }

        .top-header {
            display: flex;
            align-items: center;
            background: #ffffff;
            padding: 25px;
            gap: 20px;
            position: relative;
            box-shadow: 0 6px 16px rgba(0,0,0,0.06);
            z-index: 2;
        }

        .header-title-box {
            width: 42%;
            background: linear-gradient(135deg, #14b8a6, #0d9488);
            padding: 16px 22px;
            border-radius: 14px;
            box-shadow: var(--shadow-button-3d);
            transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.3s ease;
            transform-style: preserve-3d;
        }

        .header-title-box:active, .header-title-box:hover {
            transform: translateY(-4px) scale(1.02) rotateY(-2deg);
            box-shadow: 0 8px 0px #0d9488, 0 12px 20px rgba(0,0,0,0.25);
        }

        .header-title-box h1 {
            font-size: 26px;
            color: #ffffff;
            font-weight: 800;
            line-height: 1.3;
            text-shadow: 0 2px 5px rgba(0,0,0,0.25);
        }

        .header-title-box p {
            font-size: 14px;
            color: var(--accent-mint-soft);
            font-weight: 600;
            letter-spacing: 1px;
            margin-top: 2px;
        }

        .avatar-container {
            width: 140px;
            height: 140px;
            border-radius: 50%;
            background: #ffffff;
            padding: 5px;
            box-shadow: 0 12px 25px rgba(0,0,0,0.2), inset 0 2px 5px rgba(0,0,0,0.1);
            border: 3.5px solid var(--accent-mint);
            flex-shrink: 0;
            margin: 0 auto;
            position: relative;
            animation: mobile3DFloat 4s ease-in-out infinite alternate;
            transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            cursor: pointer;
            overflow: hidden;
            transform-style: preserve-3d;
        }

        @keyframes mobile3DFloat {
            0% {
                transform: translateY(0px) rotate(0deg);
                box-shadow: 0 10px 20px rgba(20, 184, 166, 0.3);
            }
            100% {
                transform: translateY(-8px) rotate(3deg);
                box-shadow: 0 18px 30px rgba(20, 184, 166, 0.5);
            }
        }

        .avatar-container:active {
            transform: scale(0.95) rotate(-3deg);
        }

        .avatar-container img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center;
            border-radius: 50%;
            image-rendering: -webkit-optimize-contrast;
            transform: translateZ(10px);
        }

        .contact-top-box {
            width: 38%;
            background: #f8fafc;
            padding: 16px 18px;
            border-radius: 14px;
            box-shadow: var(--shadow-3d-box), inset 0 0 0 1px #e2e8f0;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .contact-top-box:active, .contact-top-box:hover {
            transform: translateY(-3px) scale(1.01);
            box-shadow: 0 15px 25px -2px rgba(0, 0, 0, 0.15);
        }

        .contact-top-title {
            background-color: var(--accent-mint);
            color: #ffffff;
            font-size: 13px;
            font-weight: 700;
            padding: 4px 12px;
            display: inline-block;
            margin-bottom: 8px;
            border-radius: 6px;
            box-shadow: 0 3px 6px rgba(13, 148, 136, 0.3);
        }

        .contact-top-item {
            font-size: 13.5px;
            margin-bottom: 4px;
            color: var(--text-muted);
        }

        .contact-top-item strong {
            color: var(--text-main);
            font-weight: 600;
        }

        .main-content {
            display: flex;
            flex: 1;
        }

        .sidebar {
            width: 38%;
            background-color: var(--primary-dark);
            color: #ffffff;
            display: flex;
            flex-direction: column;
            box-shadow: inset -5px 0 10px rgba(0,0,0,0.15);
        }

        .sidebar-top {
            padding: 25px 20px;
            flex: 1;
        }

        .sidebar-bottom {
            background: linear-gradient(180deg, #14b8a6, #0d9488);
            padding: 22px 20px;
            color: #ffffff;
            box-shadow: 0 -4px 10px rgba(0,0,0,0.1);
        }

        .sidebar-heading {
            font-size: 14px;
            font-weight: 700;
            padding: 6px 14px;
            margin-bottom: 14px;
            margin-top: 10px;
            display: inline-block;
            border-radius: 6px;
        }

        .sidebar-top .sidebar-heading {
            background-color: var(--primary-dark-light);
            color: var(--accent-mint);
            box-shadow: var(--shadow-3d-box);
            border: 1px solid rgba(255,255,255,0.05);
        }

        .sidebar-bottom .sidebar-heading {
            background-color: var(--primary-dark);
            color: #ffffff;
            box-shadow: 0 3px 6px rgba(0,0,0,0.2);
        }

        .sidebar p {
            font-size: 13.5px;
            line-height: 1.7;
            color: #cbd5e1;
            font-weight: 400;
        }

        .signature-text {
            font-family: 'Great Vibes', cursive;
            font-size: 30px;
            color: var(--accent-mint);
            margin-top: 20px;
            text-align: center;
            text-shadow: 0 2px 4px rgba(0,0,0,0.5);
            transition: transform 0.3s ease;
        }

        .signature-text:hover {
            transform: scale(1.1) rotate(-2deg);
        }

        .signature-sub {
            font-size: 12px;
            text-align: center;
            color: #94a3b8;
        }

        .sidebar-list {
            list-style: none;
            padding: 0;
        }

        .sidebar-list li {
            font-size: 14px;
            margin-bottom: 8px;
            position: relative;
            padding-left: 20px;
            color: #f1f5f9;
            font-weight: 500;
            transition: transform 0.2s ease;
        }

        .sidebar-list li:active, .sidebar-list li:hover {
            transform: translateX(6px);
            color: #ffffff;
        }

        .sidebar-list li::before {
            content: "✔";
            position: absolute;
            left: 0;
            color: var(--primary-dark);
            font-size: 12px;
            top: 1px;
        }

        .skill-item {
            margin-bottom: 12px;
        }

        .skill-name {
            font-size: 13px;
            display: flex;
            justify-content: space-between;
            margin-bottom: 5px;
            color: #e2e8f0;
            font-weight: 500;
        }

        .progress-bar {
            height: 10px;
            background-color: #0f172a;
            border-radius: 6px;
            overflow: hidden;
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.5);
            padding: 1px;
        }

        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #14b8a6, #2dd4bf);
            border-radius: 5px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.3);
            animation: fillProgress 1.5s ease-out forwards;
            transform-origin: left;
        }

        @keyframes fillProgress {
            from { transform: scaleX(0); }
            to { transform: scaleX(1); }
        }

        .content-area {
            width: 62%;
            padding: 20px 30px 30px 30px;
            background-color: #ffffff;
        }

        .content-heading {
            background: #f1f5f9;
            color: var(--primary-dark);
            font-size: 16px;
            font-weight: 700;
            padding: 8px 16px;
            margin-top: 20px;
            margin-bottom: 14px;
            border-radius: 8px;
            border-left: 5px solid var(--accent-mint);
            box-shadow: 0 2px 5px rgba(0,0,0,0.04);
            transition: transform 0.3s ease, border-left-width 0.2s ease;
        }

        .content-heading:active, .content-heading:hover {
            transform: translateX(4px);
            border-left-width: 8px;
        }

        .info-card-3d {
            background: #ffffff;
            border-radius: 12px;
            padding: 14px 18px;
            box-shadow: var(--shadow-3d-box);
            border: 1px solid #f1f5f9;
            margin-bottom: 12px;
            transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.3s ease;
            transform-style: preserve-3d;
        }

        .info-card-3d:active, .info-card-3d:hover {
            transform: translateY(-5px) rotateX(4deg) scale(1.01);
            box-shadow: 0 16px 28px -4px rgba(0, 0, 0, 0.15);
            border-color: var(--accent-mint-soft);
        }

        .timeline-title {
            font-size: 15px;
            font-weight: 700;
            color: var(--primary-dark);
        }

        .timeline-sub {
            font-size: 13px;
            color: var(--accent-mint);
            font-weight: 600;
            margin-bottom: 4px;
        }

        .timeline-desc {
            font-size: 14px;
            color: var(--text-muted);
            line-height: 1.7;
        }

        .info-table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0 6px;
        }

        .info-table tr {
            box-shadow: 0 2px 4px rgba(0,0,0,0.02);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .info-table tr:active, .info-table tr:hover {
            transform: scale(1.01) translateX(3px);
            box-shadow: 0 4px 10px rgba(0,0,0,0.08);
        }

        .info-table td {
            padding: 8px 12px;
            font-size: 14px;
            vertical-align: top;
            background-color: #f8fafc;
            transition: background-color 0.2s ease;
        }

        .info-table tr td:first-child { border-radius: 6px 0 0 6px; }
        .info-table tr td:last-child { border-radius: 0 6px 6px 0; }

        .info-table td.label {
            font-weight: 600;
            color: var(--primary-dark);
            width: 38%;
        }

        .info-table td.value {
            color: var(--text-muted);
            width: 62%;
        }

        .footer-bar {
            background-color: var(--primary-dark);
            color: #94a3b8;
            text-align: center;
            padding: 14px;
            font-size: 13px;
            font-weight: 500;
            border-top: 1px solid rgba(255,255,255,0.05);
        }

        /* Fixed Image Modal Popup Styles */
        .image-modal {
            display: none;
            position: fixed;
            z-index: 9999;
            left: 0;
            top: 0;
            width: 100vw;
            height: 100vh;
            background-color: rgba(15, 23, 42, 0.88);
            backdrop-filter: blur(10px);
            justify-content: center;
            align-items: center;
            opacity: 0;
            overflow: hidden;
            transition: opacity 0.3s ease;
            perspective: 1000px;
        }

        .image-modal.active {
            display: flex;
            opacity: 1;
        }

        .modal-content {
            max-width: 280px;
            max-height: 70vh;
            width: auto;
            height: auto;
            border-radius: 16px;
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.6), 0 0 20px rgba(20, 184, 166, 0.4);
            border: 3.5px solid var(--accent-mint);
            transform: scale(0.6) rotateY(15deg);
            transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            object-fit: contain;
        }

        .image-modal.active .modal-content {
            transform: scale(1) rotateY(0deg);
        }

        .close-btn {
            position: absolute;
            top: 20px;
            right: 20px;
            color: #ffffff;
            font-size: 30px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.2s ease;
            line-height: 1;
            background: rgba(255, 255, 255, 0.15);
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 10000;
        }

        .close-btn:active, .close-btn:hover {
            color: var(--accent-mint);
            transform: scale(1.1) rotate(90deg);
            background: rgba(255, 255, 255, 0.25);
        }

        @media (min-width: 651px) {
            .modal-content {
                max-width: 360px;
            }
        }

        @media (max-width: 650px) {
            body { padding: 12px 6px; }
            .top-header {
                flex-direction: column;
                text-align: center;
                padding: 20px 15px;
            }
            .header-title-box, .contact-top-box {
                width: 100%;
            }
            .main-content {
                flex-direction: column;
            }
            .sidebar, .content-area {
                width: 100%;
            }
            .content-area { padding: 15px 18px 25px 18px; }
        }
    </style>
</head>
<body>

<div class="resume-container" id="mainContainer">

    <!-- Header Section -->
    <div class="top-header">
        <div class="header-title-box">
            <h1>মোঃ ওমর হানিফ</h1>
            <p>বায়োডাটা</p>
        </div>

        <div class="avatar-container" id="avatarBox">
            <img id="profileImg" src="omarhanif1.jpg" alt="ওমর হানিফ">
        </div>

        <div class="contact-top-box">
            <div class="contact-top-title">যোগাযোগ</div>
            <div class="contact-top-item"><strong>মোবাইল:</strong> ০১৭৫৩-৯০৫০০৬</div>
            <div class="contact-top-item"><strong>ই-মেইল:</strong> omarhanif5346@gmail.com</div>
            <div class="contact-top-item"><strong>ঠিকানা:</strong> জি.টি. রোড, চাঁদপুর সদর, চাঁদপুর</div>
        </div>
    </div>

    <!-- Main Content Body -->
    <div class="main-content">

        <!-- Left Sidebar -->
        <div class="sidebar">
            <div class="sidebar-top">
                <div class="sidebar-heading">সংক্ষিপ্ত পরিচয়</div>
                <p>আমি একজন সৎ, দায়িত্বশীল ও ধর্মীয় মূল্যবোধে বিশ্বাসী মানুষ। সিএসইতে ডিপ্লোমা সম্পন্ন করেছি এবং সাইবার সিকিউরিটি ও প্রযুক্তির বিভিন্ন শাখায় আগ্রহ রয়েছে। পরিবার ও সামাজিক জীবনে সুন্দর ভারসাম্য বজায় রাখতে বিশ্বাসী।</p>

                <div class="signature-text">Omar Hanif</div>
                <div class="signature-sub">সাইবার সিকিউরিটি ও তথ্যপ্রযুক্তি</div>

                <div class="sidebar-heading" style="margin-top: 25px;">ব্যক্তিগত বৈশিষ্ট্য</div>
                
                <div class="skill-item">
                    <div class="skill-name"><span>সততা ও দায়িত্ববোধ</span></div>
                    <div class="progress-bar"><div class="progress-fill" style="width: 95%;"></div></div>
                </div>
                <div class="skill-item">
                    <div class="skill-name"><span>ধর্মীয় মূল্যবোধ</span></div>
                    <div class="progress-bar"><div class="progress-fill" style="width: 90%;"></div></div>
                </div>
                <div class="skill-item">
                    <div class="skill-name"><span>পরিবারকেন্দ্রিকতা</span></div>
                    <div class="progress-bar"><div class="progress-fill" style="width: 95%;"></div></div>
                </div>
                <div class="skill-item">
                    <div class="skill-name"><span>পরিশ্রমী ও আত্মনির্ভরশীল</span></div>
                    <div class="progress-bar"><div class="progress-fill" style="width: 88%;"></div></div>
                </div>
            </div>

            <div class="sidebar-bottom">
                <div class="sidebar-heading">পেশাগত দক্ষতা</div>
                <ul class="sidebar-list">
                    <li>সাইবার সিকিউরিটি</li>
                    <li>ওয়েবসাইট সিকিউরিটি টেস্টিং</li>
                    <li>পাইথন প্রোগ্রামিং</li>
                    <li>এথিক্যাল হ্যাকিং</li>
                    <li>মেশিন লার্নিং ও ডাটা সায়েন্স</li>
                    <li>রোবোটিক্স</li>
                </ul>
            </div>
        </div>

        <!-- Right Main Content -->
        <div class="content-area">

            <!-- Personal Info -->
            <div class="content-heading">ব্যক্তিগত তথ্য</div>
            <table class="info-table">
                <tr><td class="label">পিতার নাম</td><td class="value">: মোঃ হাবিবুর রহমান বেপারী</td></tr>
                <tr><td class="label">মাতার নাম</td><td class="value">: মিসেস নূরজাহান বেগম</td></tr>
                <tr><td class="label">জন্মতারিখ</td><td class="value">: ৩১ মার্চ ২০০৩ (বয়স: ২৩ বছর)</td></tr>
                <tr><td class="label">উচ্চতা ও ওজন</td><td class="value">: ৬ ফুট (১৮৩ সেমি) | ৬৪ কেজি</td></tr>
                <tr><td class="label">রক্তের গ্রুপ</td><td class="value">: A+ (পজিটিভ)</td></tr>
                <tr><td class="label">ধর্ম ও জাতীয়তা</td><td class="value">: ইসলাম | বাংলাদেশী</td></tr>
                <tr><td class="label">বৈবাহিক অবস্থা</td><td class="value">: অবিবাহিত</td></tr>
            </table>

            <!-- Education -->
            <div class="content-heading">শিক্ষাগত যোগ্যতা</div>
            <div class="info-card-3d">
                <div class="timeline-title">ডিপ্লোমা ইন কম্পিউটার সায়েন্স অ্যান্ড টেকনোলজি</div>
                <div class="timeline-sub">ব্রাহ্মণবাড়িয়া পলিটেকনিক ইনস্টিটিউট | পাস: ২০২৫</div>
                <div class="timeline-desc">সিজিপিএ: ৩.৩৩ (৪.০০ এর মধ্যে)</div>
            </div>

            <!-- Family Info -->
            <div class="content-heading">পারিবারিক তথ্য</div>
            <table class="info-table">
                <tr><td class="label">পিতার পেশা</td><td class="value">: রেস্টুরেন্ট ব্যবসা</td></tr>
                <tr><td class="label">মাতার পেশা</td><td class="value">: গৃহিণী</td></tr>
                <tr><td class="label">ভাই-বোন</td><td class="value">: ৩ জন ভাই, ১ জন বোন</td></tr>
                <tr><td class="label">স্থায়ী ঠিকানা</td><td class="value">: জি.টি. রোড, চাঁদপুর সদর, চাঁদপুর</td></tr>
            </table>

            <!-- Hobbies & Interests -->
            <div class="content-heading">শখ ও আগ্রহ</div>
            <div class="info-card-3d">
                <div class="timeline-desc">
                    কৃত্রিম বুদ্ধিমত্তা (AI), প্রযুক্তি বিষয়ক গবেষণা, ভ্রমণ, নতুন দক্ষতা দ্রুত অর্জন করা।
                </div>
            </div>

            <!-- Life Partner Expectations -->
            <div class="content-heading">জীবনসঙ্গী সম্পর্কে প্রত্যাশা</div>
            <div class="info-card-3d" style="border-left: 4px solid var(--accent-mint);">
                <div class="timeline-desc">
                    • দ্বীনদার, নামাজি ও ধর্মীয় অনুশাসন মেনে চলেন।<br>
                    • উত্তম চরিত্রের অধিকারী ও পরিবারকে সম্মান করেন।<br>
                    • সহযোগিতাপূর্ণ, বুঝদার ও পারস্পরিক বিশ্বাসকে মূল্য দেন।
                </div>
            </div>

        </div>

    </div>

    <!-- Footer -->
    <div class="footer-bar">
        বিসমিল্লাহির রহমানির রহিম • মোঃ ওমর হানিফ
    </div>

</div>

<!-- Image Popup Modal Container -->
<div id="imgModal" class="image-modal">
    <span class="close-btn" id="closeBtn">&times;</span>
    <img class="modal-content" id="popupImage" alt="Full Image">
</div>

<script>
    const avatarBox = document.getElementById('avatarBox');
    const profileImg = document.getElementById('profileImg');
    const modal = document.getElementById('imgModal');
    const popupImage = document.getElementById('popupImage');
    const closeBtn = document.getElementById('closeBtn');
    const container = document.getElementById('mainContainer');

    let hoverTimeout;

    function showModal() {
        popupImage.src = profileImg.src;
        modal.classList.add('active');
        document.body.style.overflow = 'hidden'; // ব্যাকগ্রাউন্ড স্ক্রল বন্ধ করবে
    }

    function hideModal() {
        modal.classList.remove('active');
        document.body.style.overflow = 'auto'; // ব্যাকগ্রাউন্ড স্ক্রল পুনরায় চালু করবে
    }

    avatarBox.addEventListener('mouseenter', function() {
        hoverTimeout = setTimeout(showModal, 180); 
    });

    avatarBox.addEventListener('mouseleave', function() {
        clearTimeout(hoverTimeout);
    });

    avatarBox.addEventListener('click', function(e) {
        e.stopPropagation();
        showModal();
    });

    modal.addEventListener('click', function(e) {
        if (e.target === modal || e.target === closeBtn) {
            hideModal();
        }
    });

    document.addEventListener('keydown', function(event) {
        if (event.key === "Escape") {
            hideModal();
        }
    });

    window.addEventListener('deviceorientation', function(e) {
        if (window.innerWidth <= 650) {
            let tiltX = e.beta ? (e.beta - 45) / 10 : 0; 
            let tiltY = e.gamma ? e.gamma / 10 : 0;
            if (tiltX > 5) tiltX = 5;
            if (tiltX < -5) tiltX = -5;
            if (tiltY > 5) tiltY = 5;
            if (tiltY < -5) tiltY = -5;
            container.style.transform = `rotateX(${tiltX}deg) rotateY(${tiltY}deg)`;
        }
    });
</script>

</body>
</html>
