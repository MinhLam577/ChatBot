import pandas as pd
import os
import json
from difflib import get_close_matches
clean_data_path = "data/csv/clean_laptop_data.csv"
original_data_path = "data/csv/laptop_data.csv"
json_data_path = "data/json/question_data.json"
def load_csv(filename):
    with open(filename, 'r') as f:
        return pd.read_csv(f)
    
def load_json(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)

def save_json(filename, data):
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        
def clear_json_file(json_file):
    json_data = load_json(json_file)
    json_data["questions"] = []
    save_json(json_file, json_data)

def check_similarity(question, list_of_question):
    if question in list_of_question:
        return True
    Match =  get_close_matches(question, list_of_question, cutoff=0.9, n = 1)
    if Match is not None:
        return True
    return False

def get_list_qs_from_json_file(json_file):
    json_data = load_json(json_file)
    return [question["question"] for question in json_data["questions"]]

def find_laptop_with_highest_ScreenResolution(data, original_data):
    list_qa = []
    sr = data["ScreenResolution"].str.split("x", expand=True)
    sr.columns = ["Width", "Height"]
    sr["Width"] = sr["Width"].astype(float)
    sr["Height"] = sr["Height"].astype(float)
    sr["ScreenResolution"] = sr["Width"] * sr["Height"]
    max_sr_idx = sr["ScreenResolution"].idxmax()
    res = original_data.loc[max_sr_idx]
    columns = ["Company", "TypeName", "Inches", "ScreenResolution", "Cpu", "Ram", "Memory", "Gpu", "OpSys", "Weight", "Price"]
    convert_columns_name = ["Công ty", "Tên máy tính", "Kích thước màn hình", "Độ phân giải màn hình", "CPU", "RAM", "Bộ nhớ", "GPU", "Hệ điều hành", "Trọng lượng", "Giá"]
    s = "Máy tính có độ phân phải cao nhất"
    list_question = [f"{s} có {name.lower()} là gì?" for name in convert_columns_name]
    list_answer = [f"{res[column]}" for column, name_column in zip(columns, convert_columns_name)]
    list_question.append("\nThông tin máy tính có độ phân giải màn hình cao nhất:\n")
    list_answer.append(original_data.loc[max_sr_idx].to_string().strip())
    for i in range(len(list_question)):
        list_qa.append({"question": list_question[i], "answer": list_answer[i]})
    return list_qa

def find_laptop_with_smallest_ScreenResolution(data, original_data):
    list_qa = []
    sr = data["ScreenResolution"].str.split("x", expand=True)
    sr.columns = ["Width", "Height"]
    sr["Width"] = sr["Width"].astype(float)
    sr["Height"] = sr["Height"].astype(float)
    sr["ScreenResolution"] = sr["Width"] * sr["Height"]
    min_sr_idx = sr["ScreenResolution"].idxmin()
    res = original_data.loc[min_sr_idx]
    columns = ["Company", "TypeName", "Inches", "ScreenResolution", "Cpu", "Ram", "Memory", "Gpu", "OpSys", "Weight", "Price"]
    convert_columns_name = ["Công ty", "Tên máy tính", "Kích thước màn hình", "Độ phân giải màn hình", "CPU", "RAM", "Bộ nhớ", "GPU", "Hệ điều hành", "Trọng lượng", "Giá"]
    s = "Máy tính có độ phân phải thấp nhất"
    list_question = [f"{s} có {name.lower()} là gì?" for name in convert_columns_name]
    list_answer = [f"{res[column]}" for column, name_column in zip(columns, convert_columns_name)]
    list_question.append("\nThông tin máy tính có độ phân giải màn hình thấp nhất:\n")
    list_answer.append(original_data.loc[min_sr_idx].to_string().strip())
    for i in range(len(list_question)):
        list_qa.append({"question": list_question[i], "answer": list_answer[i]})
    return list_qa

def find_most_expensive_laptop(data, original_data):
    list_qa = []
    sr = data["Price"]
    max_sr_idx = sr.idxmax()
    res = original_data.loc[max_sr_idx]
    columns = ["Company", "TypeName", "Inches", "ScreenResolution", "Cpu", "Ram", "Memory", "Gpu", "OpSys", "Weight", "Price"]
    convert_columns_name = ["Công ty", "Tên máy tính", "Kích thước màn hình", "Độ phân giải màn hình", "CPU", "RAM", "Bộ nhớ", "GPU", "Hệ điều hành", "Trọng lượng", "Giá"]
    s = "Máy tính có giá đắt nhất"
    list_question = [f"{s} có {name.lower()} là gì?" for name in convert_columns_name]
    list_answer = [f"{res[column]}" for column, name_column in zip(columns, convert_columns_name)]
    list_question.append("\nThông tin máy tính có giá đắt nhất:\n")
    list_answer.append(original_data.loc[max_sr_idx].to_string().strip())
    for i in range(len(list_question)):
        list_qa.append({"question": list_question[i], "answer": list_answer[i]})
    return list_qa

def find_laptop_with_cheapest_price(data, original_data):
    list_qa = []
    sr = data["Price"]
    min_sr_idx = sr.idxmin()
    res = original_data.loc[min_sr_idx]
    columns = ["Company", "TypeName", "Inches", "ScreenResolution", "Cpu", "Ram", "Memory", "Gpu", "OpSys", "Weight", "Price"]
    convert_columns_name = ["Công ty", "Tên máy tính", "Kích thước màn hình", "Độ phân giải màn hình", "CPU", "RAM", "Bộ nhớ", "GPU", "Hệ điều hành", "Trọng lượng", "Giá"]
    s = "Máy tính có giá rẻ nhất"
    list_question = [f"{s} có {name.lower()} là gì?" for name in convert_columns_name]
    list_answer = [f"{res[column]}" for column, name_column in zip(columns, convert_columns_name)]
    list_question.append("\nThông tin máy tính có giá rẻ nhất:\n")
    list_answer.append(original_data.loc[min_sr_idx].to_string().strip())
    for i in range(len(list_question)):
        list_qa.append({"question": list_question[i], "answer": list_answer[i]})
    return list_qa

def find_lightest_laptop(data, original_data):
    list_qa = []
    sr = data["Weight"]
    min_sr_idx = sr.idxmin()
    res = original_data.loc[min_sr_idx]
    columns = ["Company", "TypeName", "Inches", "ScreenResolution", "Cpu", "Ram", "Memory", "Gpu", "OpSys", "Weight", "Price"]
    convert_columns_name = ["Công ty", "Tên máy tính", "Kích thước màn hình", "Độ phân giải màn hình", "CPU", "RAM", "Bộ nhớ", "GPU", "Hệ điều hành", "Trọng lượng", "Giá"]
    s = "Máy tính nhẹ nhất"
    list_question = [f"{s} có {name.lower()} là gì?" for name in convert_columns_name]
    list_answer = [f"{res[column]}" for column, name_column in zip(columns, convert_columns_name)]
    list_question.append("\nThông tin máy tính nhẹ nhất:\n")
    list_answer.append(original_data.loc[min_sr_idx].to_string().strip())
    for i in range(len(list_question)):
        list_qa.append({"question": list_question[i], "answer": list_answer[i]})
    return list_qa

def find_laptop_with_largest_weight(data, original_data):
    list_qa = []
    sr = data["Weight"]
    max_sr_idx = sr.idxmax()
    res = original_data.loc[max_sr_idx]
    columns = ["Company", "TypeName", "Inches", "ScreenResolution", "Cpu", "Ram", "Memory", "Gpu", "OpSys", "Weight", "Price"]
    convert_columns_name = ["Công ty", "Tên máy tính", "Kích thước màn hình", "Độ phân giải màn hình", "CPU", "RAM", "Bộ nhớ", "GPU", "Hệ điều hành", "Trọng lượng", "Giá"]
    s = "Máy tính có trọng lượng lớn nhất"
    list_question = [f"{s} có {name.lower()} là gì?" for name in convert_columns_name]
    list_answer = [f"{res[column]}" for column, name_column in zip(columns, convert_columns_name)]
    list_question.append("\nThông tin máy tính có trọng lượng lớn nhất:\n")
    list_answer.append(original_data.loc[max_sr_idx].to_string().strip())
    for i in range(len(list_question)):
        list_qa.append({"question": list_question[i], "answer": list_answer[i]})
    return list_qa

def find_laptop_with_largest_memory(data, original_data):
    list_qa = []
    sr = data["Memory"]
    max_sr_idx = sr.idxmax()
    res = original_data.loc[max_sr_idx]
    columns = ["Company", "TypeName", "Inches", "ScreenResolution", "Cpu", "Ram", "Memory", "Gpu", "OpSys", "Weight", "Price"]
    convert_columns_name = ["Công ty", "Tên máy tính", "Kích thước màn hình", "Độ phân giải màn hình", "CPU", "RAM", "Bộ nhớ", "GPU", "Hệ điều hành", "Trọng lượng", "Giá"]
    s = "Máy tính có bộ nhớ lớn nhất"
    list_question = [f"{s} có {name.lower()} là gì?" for name in convert_columns_name]
    list_answer = [f"{res[column]}" for column, name_column in zip(columns, convert_columns_name)]
    list_question.append("\nThông tin máy tính có bộ nhớ lớn nhất:\n")
    list_answer.append(original_data.loc[max_sr_idx].to_string().strip())
    for i in range(len(list_question)):
        list_qa.append({"question": list_question[i], "answer": list_answer[i]})
    return list_qa

def find_laptop_with_smallest_memory(data, original_data):
    list_qa = []
    sr = data["Memory"]
    min_sr_idx = sr.idxmin()
    res = original_data.loc[min_sr_idx]
    columns = ["Company", "TypeName", "Inches", "ScreenResolution", "Cpu", "Ram", "Memory", "Gpu", "OpSys", "Weight", "Price"]
    convert_columns_name = ["Công ty", "Tên máy tính", "Kích thước màn hình", "Độ phân giải màn hình", "CPU", "RAM", "Bộ nhớ", "GPU", "Hệ điều hành", "Trọng lượng", "Giá"]
    s = "Máy tính có bộ nhớ thấp nhất"
    list_question = [f"{s} có {name.lower()} là gì?" for name in convert_columns_name]
    list_answer = [f"{res[column]}" for column, name_column in zip(columns, convert_columns_name)]
    list_question.append("\nThông tin máy tính có bộ nhớ thấp nhất:\n")
    list_answer.append(original_data.loc[min_sr_idx].to_string().strip())
    for i in range(len(list_question)):
        list_qa.append({"question": list_question[i], "answer": list_answer[i]})
    return list_qa
    
def find_laptop_with_largest_inch(data, original_data):
    list_qa = []
    sr = data["Inches"]
    max_sr_idx = sr.idxmax()
    res = original_data.loc[max_sr_idx]
    columns = ["Company", "TypeName", "Inches", "ScreenResolution", "Cpu", "Ram", "Memory", "Gpu", "OpSys", "Weight", "Price"]
    convert_columns_name = ["Công ty", "Tên máy tính", "Kích thước màn hình", "Độ phân giải màn hình", "CPU", "RAM", "Bộ nhớ", "GPU", "Hệ điều hành", "Trọng lượng", "Giá"]
    s = "Máy tính có kích thước màn hình lớn nhất"
    list_question = [f"{s} có {name.lower()} là gì?" for name in convert_columns_name]
    list_answer = [f"{res[column]}" for column, name_column in zip(columns, convert_columns_name)]
    list_question.append("\nThông tin máy tính có kích thước màn hình lớn nhất:\n")
    list_answer.append(original_data.loc[max_sr_idx].to_string().strip())
    for i in range(len(list_question)):
        list_qa.append({"question": list_question[i], "answer": list_answer[i]})
    return list_qa

def find_laptop_with_smallest_inch(data, original_data):
    list_qa = []
    sr = data["Inches"]
    min_sr_idx = sr.idxmin()
    res = original_data.loc[min_sr_idx]
    columns = ["Company", "TypeName", "Inches", "ScreenResolution", "Cpu", "Ram", "Memory", "Gpu", "OpSys", "Weight", "Price"]
    convert_columns_name = ["Công ty", "Tên máy tính", "Kích thước màn hình", "Độ phân giải màn hình", "CPU", "RAM", "Bộ nhớ", "GPU", "Hệ điều hành", "Trọng lượng", "Giá"]
    s = "Máy tính có kích thước màn hình nhỏ nhất"
    list_question = [f"{s} có {name.lower()} là gì?" for name in convert_columns_name]
    list_answer = [f"{res[column]}" for column, name_column in zip(columns, convert_columns_name)]
    list_question.append("\nThông tin máy tính có kích thước màn hình nhỏ nhất:\n")
    list_answer.append(original_data.loc[min_sr_idx].to_string().strip())
    for i in range(len(list_question)):
        list_qa.append({"question": list_question[i], "answer": list_answer[i]})
    return list_qa

def find_laptop_with_largest_ram(data, original_data):
    list_qa = []
    sr = data["Ram"]
    max_sr_idx = sr.idxmax()
    res = original_data.loc[max_sr_idx]
    columns = ["Company", "TypeName", "Inches", "ScreenResolution", "Cpu", "Ram", "Memory", "Gpu", "OpSys", "Weight", "Price"]
    convert_columns_name = ["Công ty", "Tên máy tính", "Kích thước màn hình", "Độ phân giải màn hình", "CPU", "RAM", "Bộ nhớ", "GPU", "Hệ điều hành", "Trọng lượng", "Giá"]
    s = "Máy tính có RAM lớn nhất"
    list_question = [f"{s} có {name.lower()} là gì?" for name in convert_columns_name]
    list_answer = [f"{res[column]}" for column, name_column in zip(columns, convert_columns_name)]
    list_question.append("\nThông tin máy tính có RAM lớn nhất:\n")
    list_answer.append(original_data.loc[max_sr_idx].to_string().strip())
    for i in range(len(list_question)):
        list_qa.append({"question": list_question[i], "answer": list_answer[i]})
    return list_qa

def find_laptop_with_smallest_ram(data, original_data):
    list_qa = []
    sr = data["Ram"]
    min_sr_idx = sr.idxmin()
    res = original_data.loc[min_sr_idx]
    columns = ["Company", "TypeName", "Inches", "ScreenResolution", "Cpu", "Ram", "Memory", "Gpu", "OpSys", "Weight", "Price"]
    convert_columns_name = ["Công ty", "Tên máy tính", "Kích thước màn hình", "Độ phân giải màn hình", "CPU", "RAM", "Bộ nhớ", "GPU", "Hệ điều hành", "Trọng lượng", "Giá"]
    s = "Máy tính có RAM nhỏ nhất"
    list_question = [f"{s} có {name.lower()} là gì?" for name in convert_columns_name]
    list_answer = [f"{res[column]}" for column, name_column in zip(columns, convert_columns_name)]
    list_question.append("\nThông tin máy tính có RAM nhỏ nhất:\n")
    list_answer.append(original_data.loc[min_sr_idx].to_string().strip())
    for i in range(len(list_question)):
        list_qa.append({"question": list_question[i], "answer": list_answer[i]})
    return list_qa

def find_laptop_with_largest_cpu(data, original_data):
    list_qa = []
    sr = data["Cpu"]
    max_sr_idx = sr.idxmax()
    res = original_data.loc[max_sr_idx]
    columns = ["Company", "TypeName", "Inches", "ScreenResolution", "Cpu", "Ram", "Memory", "Gpu", "OpSys", "Weight", "Price"]
    convert_columns_name = ["Công ty", "Tên máy tính", "Kích thước màn hình", "Độ phân giải màn hình", "CPU", "RAM", "Bộ nhớ", "GPU", "Hệ điều hành", "Trọng lượng", "Giá"]
    s = "Máy tính có CPU mạnh nhất"
    list_question = [f"{s} có {name.lower()} là gì?" for name in convert_columns_name]
    list_answer = [f"{res[column]}" for column, name_column in zip(columns, convert_columns_name)]
    list_question.append("\nThông tin máy tính có CPU mạnh nhất:\n")
    list_answer.append(original_data.loc[max_sr_idx].to_string().strip())
    for i in range(len(list_question)):
        list_qa.append({"question": list_question[i], "answer": list_answer[i]})
    return list_qa

def find_laptop_with_smallest_cpu(data, original_data):
    list_qa = []
    sr = data["Cpu"]
    min_sr_idx = sr.idxmin()
    res = original_data.loc[min_sr_idx]
    columns = ["Company", "TypeName", "Inches", "ScreenResolution", "Cpu", "Ram", "Memory", "Gpu", "OpSys", "Weight", "Price"]
    convert_columns_name = ["Công ty", "Tên máy tính", "Kích thước màn hình", "Độ phân giải màn hình", "CPU", "RAM", "Bộ nhớ", "GPU", "Hệ điều hành", "Trọng lượng", "Giá"]
    s = "Máy tính có CPU yếu nhất"
    list_question = [f"{s} có {name.lower()} là gì?" for name in convert_columns_name]
    list_answer = [f"{res[column]}" for column, name_column in zip(columns, convert_columns_name)]
    list_question.append("\nThông tin máy tính có CPU yếu nhất:\n")
    list_answer.append(original_data.loc[min_sr_idx].to_string().strip())
    for i in range(len(list_question)):
        list_qa.append({"question": list_question[i], "answer": list_answer[i]})
    return list_qa

def get_all_OpSys(data):
    list_qa = []
    qs = []
    ans = []
    question = "Có những hệ điều hành nào?"
    answer = "Có những hệ điều hành sau: "
    for OpSys in data["OpSys"].unique():
        answer += f"{OpSys}, "
    answer = answer[:-2]
    qs.append(question)
    ans.append(answer)
    for OpSys in data["OpSys"].unique():
        question = f"Có bao nhiêu máy tính có hệ điều hành {OpSys}?"
        answer = f"{len(data[data['OpSys'] == OpSys])} máy"
        qs.append(question)
        ans.append(answer)
    for i in range(len(qs)):
        list_qa.append({"question": qs[i], "answer": ans[i]})
    return list_qa, data["OpSys"].unique()

def get_all_Company(data):
    list_qa = []
    qs = []
    ans = []
    question = "Có những hãng máy tính nào?"
    answer = "Có những hãng máy tính sau: \n"
    for Company in data["Company"].unique():
        answer += f"{Company}, "
    answer = answer[:-2]
    qs.append(question)
    ans.append(answer)
    for Company in data["Company"].unique():
        question = f"Có bao nhiêu máy tính của hãng {Company}?"
        answer = f"{len(data[data['Company'] == Company])} máy"
        qs.append(question)
        ans.append(answer)
    for i in range(len(qs)):
        list_qa.append({"question": qs[i], "answer": ans[i]})
    return list_qa, data["Company"].unique()

def get_all_typename(data):
    list_qa = []
    qs = []
    ans = []
    question = "Có những dòng máy tính nào?"
    answer = "Có những dòng máy tính sau: \n"
    for TypeName in data["TypeName"].unique():
        answer += f"{TypeName}, "
    answer = answer[:-2]
    qs.append(question)
    ans.append(answer)
    for TypeName in data["TypeName"].unique():
        question = f"Có bao nhiêu máy tính của dòng {TypeName}?"
        answer = f"{len(data[data['TypeName'] == TypeName])} máy"
        qs.append(question)
        ans.append(answer)
    for i in range(len(qs)):
        list_qa.append({"question": qs[i], "answer": ans[i]})
    return list_qa, data["TypeName"].unique()

def get_lap_count_by_company(data):
    list_qa = []
    qs = []
    ans = []
    question = "Có bao nhiêu máy tính của mỗi hãng?"
    answer = "Số lượng máy tính của mỗi hãng: \n"
    for Company in data["Company"].unique():
        answer += f"{Company}: {len(data[data['Company'] == Company])} máy, "
    answer = answer[:-2]
    qs.append(question)
    ans.append(answer)
    for Company in data["Company"].unique():
        question = f"Có bao nhiêu máy tính của hãng {Company}?"
        answer = f"{len(data[data['Company'] == Company])} máy"
        qs.append(question)
        ans.append(answer)
    for i in range(len(qs)):
        list_qa.append({"question": qs[i], "answer": ans[i]})
    return list_qa

def get_lap_count_by_typename(data):
    list_qa = []
    qs = []
    ans = []
    question = "Có bao nhiêu máy tính của mỗi dòng?"
    answer = "Số lượng máy tính của mỗi dòng: \n"
    for TypeName in data["TypeName"].unique():
        answer += f"{TypeName}: {len(data[data['TypeName'] == TypeName])} máy, "
    answer = answer[:-2]
    qs.append(question)
    ans.append(answer)
    for TypeName in data["TypeName"].unique():
        question = f"Có bao nhiêu máy tính của dòng {TypeName}?"
        answer = f"{len(data[data['TypeName'] == TypeName])} máy"
        qs.append(question)
        ans.append(answer)
    for i in range(len(qs)):
        list_qa.append({"question": qs[i], "answer": ans[i]})
    return list_qa

def get_lap_count_by_OpSys(data):
    list_qa = []
    qs = []
    ans = []
    question = "Có bao nhiêu máy tính của mỗi hệ điều hành?"
    answer = "Số lượng máy tính của mỗi hệ điều hành: \n"
    for OpSys in data["OpSys"].unique():
        answer += f"{OpSys}: {len(data[data['OpSys'] == OpSys])} máy, "
    answer = answer[:-2]
    qs.append(question)
    ans.append(answer)
    for OpSys in data["OpSys"].unique():
        question = f"Có bao nhiêu máy tính của hệ điều hành {OpSys}?"
        answer = f"{len(data[data['OpSys'] == OpSys])} máy"
        qs.append(question)
        ans.append(answer)
    for i in range(len(qs)):
        list_qa.append({"question": qs[i], "answer": ans[i]})
    return list_qa

def get_lap_count_by_ScreenResolution(data):
    list_qa = []
    qs = []
    ans = []
    question = "Có bao nhiêu máy tính có cùng độ phân giải màn hình?"
    answer = "Số lượng máy tính có cùng độ phân giải màn hình: \n"
    for ScreenResolution in data["ScreenResolution"].unique():
        answer += f"{ScreenResolution}: {len(data[data['ScreenResolution'] == ScreenResolution])} máy, "
    answer = answer[:-2]
    qs.append(question)
    ans.append(answer)
    for ScreenResolution in data["ScreenResolution"].unique():
        question = f"Có bao nhiêu máy tính có độ phân giải màn hình {ScreenResolution}?"
        answer = f"{len(data[data['ScreenResolution'] == ScreenResolution])} máy"
        qs.append(question)
        ans.append(answer)
    for i in range(len(qs)):
        list_qa.append({"question": qs[i], "answer": ans[i]})
    return list_qa

def get_lap_count_by_Weight(data):
    list_qa = []
    qs = []
    ans = []
    question = "Có bao nhiêu máy tính có cùng trọng lượng?"
    answer = "Số lượng máy tính có cùng trọng lượng: \n"
    for Weight in data["Weight"].unique():
        answer += f"{Weight}: {len(data[data['Weight'] == Weight])} máy, "
    answer = answer[:-2]
    qs.append(question)
    ans.append(answer)
    for Weight in data["Weight"].unique():
        question = f"Có bao nhiêu máy tính có trọng lượng {Weight}?"
        answer = f"{len(data[data['Weight'] == Weight])} máy"
        qs.append(question)
        ans.append(answer)
    for i in range(len(qs)):
        list_qa.append({"question": qs[i], "answer": ans[i]})
    return list_qa

def get_lap_count_by_Ram(data):
    list_qa = []
    qs = []
    ans = []
    question = "Có bao nhiêu máy tính có cùng dung lượng RAM?"
    answer = "Số lượng máy tính có cùng dung lượng RAM: \n"
    for Ram in data["Ram"].unique():
        answer += f"{Ram}: {len(data[data['Ram'] == Ram])} máy, "
    answer = answer[:-2]
    qs.append(question)
    ans.append(answer)
    for Ram in data["Ram"].unique():
        question = f"Có bao nhiêu máy tính có dung lượng RAM {Ram}?"
        answer = f"{len(data[data['Ram'] == Ram])} máy"
        qs.append(question)
        ans.append(answer)
    for i in range(len(qs)):
        list_qa.append({"question": qs[i], "answer": ans[i]})
    return list_qa

def get_lap_count_by_Cpu(data):
    list_qa = []
    qs = []
    ans = []
    question = "Có bao nhiêu máy tính có cùng CPU?"
    answer = "Số lượng máy tính có cùng CPU: \n"
    for Cpu in data["Cpu"].unique():
        answer += f"{Cpu}: {len(data[data['Cpu'] == Cpu])} máy, "
    answer = answer[:-2]
    qs.append(question)
    ans.append(answer)
    for Cpu in data["Cpu"].unique():
        question = f"Có bao nhiêu máy tính có CPU {Cpu}?"
        answer = f"{len(data[data['Cpu'] == Cpu])} máy"
        qs.append(question)
        ans.append(answer)
    for i in range(len(qs)):
        list_qa.append({"question": qs[i], "answer": ans[i]})
    return list_qa

def get_lap_count_by_Gpu(data):
    list_qa = []
    qs = []
    ans = []
    question = "Có bao nhiêu máy tính có cùng GPU?"
    answer = "Số lượng máy tính có cùng GPU: \n"
    for Gpu in data["Gpu"].unique():
        answer += f"{Gpu}: {len(data[data['Gpu'] == Gpu])} máy, "
    answer = answer[:-2]
    qs.append(question)
    ans.append(answer)
    for Gpu in data["Gpu"].unique():
        question = f"Có bao nhiêu máy tính có GPU {Gpu}?"
        answer = f"{len(data[data['Gpu'] == Gpu])} máy"
        qs.append(question)
        ans.append(answer)
    for i in range(len(qs)):
        list_qa.append({"question": qs[i], "answer": ans[i]})
    return list_qa

def get_lap_count_by_Inches(data):
    list_qa = []
    qs = []
    ans = []
    question = "Có bao nhiêu máy tính có cùng kích thước màn hình?"
    answer = "Số lượng máy tính có cùng kích thước màn hình: \n"
    for Inches in data["Inches"].unique():
        answer += f"{Inches}: {len(data[data['Inches'] == Inches])} máy, "
    answer = answer[:-2]
    qs.append(question)
    ans.append(answer)
    for Inches in data["Inches"].unique():
        question = f"Có bao nhiêu máy tính có kích thước màn hình {Inches}?"
        answer = f"{len(data[data['Inches'] == Inches])} máy"
        qs.append(question)
        ans.append(answer)
    for i in range(len(qs)):
        list_qa.append({"question": qs[i], "answer": ans[i]})
    return list_qa

def get_all_Weight(data):
    list_qa = []
    question = "Có những trọng lượng nào?"
    answer = "Có những trọng lượng sau: "
    for Weight in data["Weight"].unique():
        answer += f"{Weight}, "
    answer = answer[:-2]
    list_qa.append({"question": question, "answer": answer})
    return list_qa, data["Weight"].unique()

def get_all_Ram(data):
    list_qa = []
    question = "Có những dung lượng RAM nào?"
    answer = "Có những dung lượng RAM sau: "
    for Ram in data["Ram"].unique():
        answer += f"{Ram}, "
    answer = answer[:-2]
    list_qa.append({"question": question, "answer": answer})
    return list_qa, data["Ram"].unique()

def get_all_Cpu(data):
    list_qa = []
    question = "Có những CPU nào?"
    answer = "Có những CPU sau: "
    for Cpu in data["Cpu"].unique():
        answer += f"{Cpu}, "
    answer = answer[:-2]
    list_qa.append({"question": question, "answer": answer})
    return list_qa, data["Cpu"].unique()

def get_all_Gpu(data):
    list_qa = []
    question = "Có những GPU nào?"
    answer = "Có những GPU sau: "
    for Gpu in data["Gpu"].unique():
        answer += f"{Gpu}, "
    answer = answer[:-2]
    list_qa.append({"question": question, "answer": answer})
    return list_qa, data["Gpu"].unique()

def get_all_ScreenResolution(data):
    list_qa = []
    question = "Có những độ phân giải màn hình nào?"
    answer = "Có những độ phân giải màn hình sau: "
    for ScreenResolution in data["ScreenResolution"].unique():
        answer += f"{ScreenResolution}, "
    answer = answer[:-2]
    list_qa.append({"question": question, "answer": answer})
    return list_qa, data["ScreenResolution"].unique()

def get_all_Inches(data):
    list_qa = []
    question = "Có những kích thước màn hình nào?"
    answer = "Có những kích thước màn hình sau: "
    for Inches in data["Inches"].unique():
        answer += f"{Inches}, "
    answer = answer[:-2]
    list_qa.append({"question": question, "answer": answer})
    return list_qa, data["Inches"].unique()

def get_all_Memory(data):
    list_qa = []
    question = "Có những dung lượng bộ nhớ nào?"
    answer = "Có những dung lượng bộ nhớ sau: "
    for Memory in data["Memory"].unique():
        answer += f"{Memory}, "
    answer = answer[:-2]
    list_qa.append({"question": question, "answer": answer})
    return list_qa, data["Memory"].unique()

clean_data = load_csv(clean_data_path)
original_data = load_csv(original_data_path)
original_data = original_data.drop(columns=["Unnamed: 0"])
json_data = load_json(json_data_path)

functions_finds = [find_laptop_with_highest_ScreenResolution, find_laptop_with_smallest_ScreenResolution, find_most_expensive_laptop, find_laptop_with_cheapest_price, find_lightest_laptop, find_laptop_with_largest_weight, find_laptop_with_largest_memory, find_laptop_with_smallest_memory, find_laptop_with_largest_inch, find_laptop_with_smallest_inch, find_laptop_with_largest_ram, find_laptop_with_smallest_ram, find_laptop_with_largest_cpu, find_laptop_with_smallest_cpu]

functions_get_all = [get_all_Company, get_all_typename, get_all_OpSys, get_all_ScreenResolution, get_all_Weight, get_all_Ram, get_all_Cpu, get_all_Gpu, get_all_Inches, get_all_Memory]

functions_get_lap_count = [get_lap_count_by_company, get_lap_count_by_typename, get_lap_count_by_OpSys, get_lap_count_by_ScreenResolution, get_lap_count_by_Weight, get_lap_count_by_Ram, get_lap_count_by_Cpu, get_lap_count_by_Gpu, get_lap_count_by_Inches]

list_qa_json_file = get_list_qs_from_json_file(json_data_path)

for function in functions_finds:
    list_qa = function(clean_data, original_data)
    list_qa_need = []
    for qa in list_qa:
        if not check_similarity(qa, list_qa_json_file):
            list_qa_need.append(qa)
    for qa in list_qa_need:
        qa['answer'] = f'"""{qa["answer"]}"""'
    json_data["questions"].extend(list_qa_need)
    
for function in functions_get_all:
    list_qa, _ = function(clean_data)
    list_qa_need = []
    for qa in list_qa:
        if not check_similarity(qa, list_qa_json_file):
            list_qa_need.append(qa)
    for qa in list_qa_need:
        qa['answer'] = f'"""{qa["answer"]}"""'
    json_data["questions"].extend(list_qa_need)
    
for function in functions_get_lap_count:
    list_qa = function(clean_data)
    list_qa_need = []
    for qa in list_qa:
        if not check_similarity(qa, list_qa_json_file):
            list_qa_need.append(qa)
    for qa in list_qa_need:
        qa['answer'] = f'"""{qa["answer"]}"""'
    json_data["questions"].extend(list_qa_need)

save_json(json_data_path, json_data)
print("Done")