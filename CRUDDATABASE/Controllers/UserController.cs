using CRUDDATABASE.DAL;
using CRUDDATABASE.Repository;
using Microsoft.AspNetCore.Mvc;

namespace CRUDDATABASE.Controllers
{
    public class UserController : Controller
    {
        private readonly IUnitOfWork _unitOfWork;

        public UserController(IUnitOfWork unitOfWork)
        {
            _unitOfWork = unitOfWork;
        }

        public async Task<IActionResult> Index()
        {
            var users = await _unitOfWork.userRepository.GetUsers();
            return View(users);
        }

        public IActionResult Create()
        {
            return View();
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
		public async Task<IActionResult> Create([Bind("IdUser", "NameUser", "Username", "PassUser", "Phone", "Email", "Facebook", "AccessUser")] QlUser user)
        {
            if (ModelState.IsValid)
            {
                await _unitOfWork.userRepository.Add(user);
                await _unitOfWork.SaveASync();
                return RedirectToAction("Index");
            }
            return View(user);
        }

        public async Task<IActionResult> Edit(int id)
        {
            if (id == 0)
            {
                return View();
            }
            var user = await _unitOfWork.userRepository.GetUserById(id);
            if (user == null)
            {
                return View();
            }
            return View(user);
        }



		[HttpPost]
		[ValidateAntiForgeryToken]
		public async Task<IActionResult> Edit(int id, [Bind("IdUser", "NameUser", "Username", "PassUser", "Phone", "Email", "Facebook", "AccessUser")] QlUser user)
		{
			if (id != user.IdUser)
			{
				return View();
			}
			if (ModelState.IsValid)
			{
				await _unitOfWork.userRepository.Update(user);
				await _unitOfWork.SaveASync();
				return RedirectToAction("Index");
			}
			return View(user);
		}


		public async Task<IActionResult> Delete(int id)
		{
			if (id == 0)
			{
				return View();
			}
			var user = await _unitOfWork.userRepository.GetUserById(id);
			if (user == null)
			{
				return View();
			}
			return View(user);
		}


		[HttpPost]
		[ValidateAntiForgeryToken, ActionName("Delete")]
		public async Task<IActionResult> DeleteConfirmed(int id, [Bind("IdUser", "NameUser", "Username", "PassUser", "Phone", "Email", "Facebook", "AccessUser")] QlUser user)
		{
			if (id != user.IdUser)
			{
				return View();
			}
			if (ModelState.IsValid)
			{
				await _unitOfWork.userRepository.Delete(id);
				await _unitOfWork.SaveASync();
				return RedirectToAction("Index");
			}
			return View(user);
		}


	}
}
