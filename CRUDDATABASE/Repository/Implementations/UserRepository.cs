using CRUDDATABASE.DAL;
using Microsoft.EntityFrameworkCore;

namespace CRUDDATABASE.Repository.Implementations
{
    public class UserRepository : IUserRepository
    {
        private readonly ApptvcakoiContext _apptvcakoiContext;

        public UserRepository(ApptvcakoiContext apptvcakoiContext)
        {
            _apptvcakoiContext = apptvcakoiContext;
        }

        public async Task Add(QlUser user)
        {
            _apptvcakoiContext.QlUsers.Add(user);
            await _apptvcakoiContext.SaveChangesAsync();
        }

        public async Task Delete(int id)
        {
            var user = await _apptvcakoiContext.QlUsers.FindAsync(id);
            if (user != null)
            {
                _apptvcakoiContext.Remove(user);
                await _apptvcakoiContext.SaveChangesAsync();
            }
        }

		public async Task<QlUser> GetUserById(int id)
		{
			return await _apptvcakoiContext.QlUsers.FindAsync(id);
		}

		public async Task<IEnumerable<QlUser>> GetUsers()
        {
            return await _apptvcakoiContext.QlUsers.ToListAsync();
        }

        public async Task Update(QlUser user)
        {
            _apptvcakoiContext.Entry(user).State = EntityState.Modified;
            await _apptvcakoiContext.SaveChangesAsync();
        }
    }
}
