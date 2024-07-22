import json

#Import hàm get_close_matches để hỗ trợ việc tìm câu trả lời được chính xác hơn
from difflib import get_close_matches

#Tạo hàm load_knowledge_base với file_path để mở tệp và đọc thông tin từ tệp Json
def load_knowledge_base(file_path: str):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data: dict = json.load(file)
        return data 
    #Nếu tệp không tồn tại hoặc dữ liệu JSON không hợp lệ, hàm sẽ in ra thông báo lỗi và trả về None
    except FileNotFoundError:
        print("File không tồn tại. Vui lòng kiểm tra lại đường dẫn.")
        return None
    except json.JSONDecodeError:
        print("Dữ liệu JSON không hợp lệ. Vui lòng kiểm tra lại dữ liệu.")
        return None

#Tạo hàm save_knowledge_base để lưu dữ liệu vào tệp JSON bằng file_path. Dữ liệu được định dạng với thụt lề là 2
def save_knowledge_base(file_path: str, data: dict):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2)
    #Nếu có lỗi xảy ra khi lưu dữ liệu, hàm sẽ in ra thông báo lỗi.        
    except Exception as e:
        print(f"Không thể lưu dữ liệu: {str(e)}")

#Tạo hàm tìm kiếm câu hỏi tốt nhất phù hợp với "user_question" từ danh sách "question" bằng cách sử dụng hàm get_close_matches
def find_best_match(user_question: str, question: list[str]) -> str | None: #Nếu không tìm thấy kết quả phù hợp, hàm sẽ trả về None
    matches: list = get_close_matches(user_question, question, n=1, cutoff=0.6)
    return matches[0] if matches else None

#Tạo hàm get_answer_for_question để tìm kiếm câu trả lời cho question trong knowledge_base bằng cách sử dụng hàm get()
def get_answer_for_question(question: str, knowledge_base: dict) -> str | None: #Nếu không tìm thấy câu trả lời, hàm sẽ trả về None
    return knowledge_base.get(question)

#Tiến hành tạo hàm chính của chatbot
def chat_bot():
    #Bắt đầu tải dữ liệu từ file Json bằng cách tạo biến knowledge_base
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')
    #Nếu không thể tải được bất kỳ dữ liệu nào từ file Json, hàm chat_bot() sẽ kết thúc ngay lập tức
    if knowledge_base is None:
        return
    #Đưa hàm chat_bot() vào một vòng lặp vô hạn. Điều này sẽ giúp nó liên tục nhận và trả lời các câu hỏi từ người dùng
    while True:
        user_input: str = input('Bạn: ')
        #Nếu người dùng nhập ‘quit’, vòng lặp sẽ kết thúc và hàm chat_bot() sẽ kết thúc
        if user_input.lower() == 'quit':
            break
        #Hàm chat_bot() sau đó tìm câu hỏi tốt nhất phù hợp với câu hỏi của người dùng bằng cách gọi hàm find_best_match()
        best_match: str | None = find_best_match(user_input, knowledge_base.keys())
        #Nếu tìm thấy một câu hỏi phù hợp, chatbot sẽ trả lời dựa trên dữ liệu từ file Json
        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            print(f'Chatbot: {answer}')
        #Ngược lại, chatbot sẽ đưa ra yêu cầu nhất định bắt người dùng chọn
        else:
            print('Chatbot: Tôi không biết câu trả lời. Bạn có thể dạy cho tôi không?')
            new_answer: str = input('Nhập câu trả lời hoặc ghi "skip" để bỏ qua: ')
            #Nếu người dùng nhập một câu trả lời (thay vì nhập ‘skip’), hàm chat_bot() sẽ thêm câu hỏi và câu trả lời mới vào file Json
            if new_answer.lower() != 'skip':
                knowledge_base[user_input] = new_answer
                save_knowledge_base('knowledge_base.json', knowledge_base)
                print('Chatbot: Cảm ơn bạn! Tôi đã biết cách trả lời.')

if __name__ == '__main__':
    chat_bot()
