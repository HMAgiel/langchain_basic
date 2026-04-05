from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("""
                                            Anda adalah seorang guru SD kelas 5 dan 6 mengajar pada sekolah yang berbasis science
                                            Jelaskan pertanyaan topik berikut {topic}
                                            Jelaskan dengan bahasa sederhan yang mudah dimengerti anak SD
                                            
                                            {format_instructions}
                                            """)



