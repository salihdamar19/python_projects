import asyncio
import edge_tts

async def sesli_oku():
    metin = "SPK haftalık bültenine göre, Kurul, Çitlekçi Mağazacılık Gıda AŞ'nin 73,70 liradan, Teknika Plast Teknik Kalıp Plastik Sanayi ve Ticaret AŞ'nin 85,40 liradan, Türker Vangölü Enerji Yatırım AŞ'nin 136 liradan, Kapeks Kimya Sanayi AŞ'nin 94 liradan halka arzını uygun buldu."
    ses = edge_tts.Communicate(metin, voice="tr-TR-AhmetNeural")
    await ses.save("haber.mp3")

asyncio.run(sesli_oku())