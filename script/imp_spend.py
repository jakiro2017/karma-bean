# Import necessary modules
import os
import django
import sys
sys.path.append("/dev/shm/karma-bean/")
# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "karma_bean.settings")
django.setup()

# Import your model
from karma_bean.tasks.models import Task, SpendPoint

# Your input string
input_string = """
Xem youtube giải trí	YTB	Xem youtube ngoài giờ ăn, kể cả quân sự	1
Xem tiktok giải trí	TIKTOK	Xem tiktok ngoài giờ ăn, kể cả quân sự	1
Tự ăn liên hoan	ANLIENHOAN	Tự ăn liên hoan do thèm	1
Chi hưởng thụ khác	HUONGTHU	Chi cho các hoạt động hưởng thụ, chơi bời ko nhằm mở rộng net, mất tiền linh tinh đo đi muộn, đánh rơi... Làm đồ hỏng hết hạn lãng phí	1
Task đầu tư lỗ nhỏ	DAUTULONHO	Các khoản đầu tư có lỗ < 10u	1
Task đầu tư lỗ lớn	DAUTULOLON	Các khoản đầu tư có lỗ > 10u	1
Vay nợ	VAY	Có các hoạt động tài chính dẫn đến phải vay nợ	2
Chơi game	GAME	Chơi điện tử hoặc xem chơi điện tử, trừ lúc ngủ 30p	2
"""

# Split the input string into lines
lines = input_string.strip().split('\n')

# Process each line
for line in lines:
    # Split the line into fields
    fields = line.split('\t')

    # Extract values
    name = fields[0]
    code = fields[1]
    explanation = fields[2]
    generic_demand = float(fields[3])
    is_income = False

    # Create and save the SpendPoint instance
    spend_point = SpendPoint(
        name=name,
        code=code,
        explaination=explanation,
        generic_demand=generic_demand,
        isIncome=is_income
    )
    spend_point.save()

print("Data insertion completed.")
